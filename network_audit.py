from netmiko import ConnectHandler
from getpass import getpass
from netmiko import NetmikoAuthenticationException
from netmiko import NetmikoTimeoutException
import csv

from pathlib import Path
reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

command_list = [("hostname","show running-config | include ^hostname"),("interfaces","show ip interface brief"),("routes", "show ip route"),("running-config","show running-config")]
username = input("enter the username:")
pwd = getpass("enter the password")
with open("inventory.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    device_list = list(reader)
    print(device_list)
    audit_results = []
    for device in device_list:
        print(device["name"])
        print(device["host"])    
        obj = None
        print("No any device connected yet")
        try:
            obj = ConnectHandler(host=device["host"], username=username, password=pwd,device_type=device["device_type"].strip())
            print(f"connected to {device["name"]}" + "\n")
            for label,command in command_list:
                output = obj.send_command(command)
                with open(reports_dir/f"{device["name"]}_{label}.txt" , "w") as file:
                    file.write(f"Device: {device["name"]}\n")
                    file.write(f"command: {command}\n")
                    file.write("*"*50 + "\n")
                    file.write(output +"\n")
                    file.write("*"*50 + "\n")    
            audit_results.append({"device": device["name"],"ip_address": device["host"],"audit_status": "SUCCESS","commands_successful": len(command_list),"commands_failed": 0})                         
        except NetmikoAuthenticationException:
            print(f"Authentication failed for {device["name"]}")
            audit_results.append({"device": device["name"],"ip_address": device["host"],"audit_status": "FAILED","commands_successful": 0 ,"commands_failed": len(command_list)})                         
        except NetmikoTimeoutException:
            print(f"connection timed out for {device["name"]}")    
        finally:
            if obj is not None:
                obj.disconnect() 
with open("audit_summary.csv","w", newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["device","ip_address","audit_status","commands_successful","commands_failed"])   
    writer.writeheader()
    writer.writerows(audit_results)          








# 
