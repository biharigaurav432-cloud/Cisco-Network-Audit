# Cisco Network Audit Automation

## 1. Project Overview

This project automates the collection of operational information from Cisco network devices using Python and Netmiko.

Instead of manually connecting to each router and executing commands one by one, the script reads device details from an inventory file, connects to each device over SSH, executes predefined show commands, and saves the command output into individual report files.

The project also generates a CSV summary showing the audit status of each device and the number of successful and failed commands.

## 2. Project Objectives

* Automate SSH connections to multiple Cisco routers.
* Read device information from a CSV inventory.
* Execute multiple show commands on each router.
* Save command output into individual text files.
* Handle common connection errors using exception handling.
* Generate a summary report for all audited devices.
* Disconnect from devices after the audit.

## 3. Technologies Used

* **Python:** Main programming language.
* **Netmiko:** Connects to network devices and executes commands over SSH.
* **CSV module:** Reads the inventory and generates the audit summary.
* **Pathlib:** Handles file and directory paths.
* **Getpass:** Accepts passwords without displaying them as normal terminal text.

## 4. Project Structure

Cisco_Network_Audit/

* inventory.csv — Contains the device inventory.
* network_audit.py — Main automation script.
* audit_summary.csv — Summary of the audit results.
* README.txt — Project documentation.
* reports/ — Directory containing individual command output reports.

Example report files:

* R1_hostname.txt
* R1_interfaces.txt
* R1_routes.txt
* R1_running-config.txt
* R2_hostname.txt
* R3_interfaces.txt

The actual report files depend on the device names and commands configured in the script.

## 5. Device Inventory

The inventory is maintained in `inventory.csv`.

Example:

name,host,device_type
R1,192.168.58.10,cisco_ios
R2,192.168.58.11,cisco_ios
R3,192.168.58.12,cisco_ios

Each column represents:

* **name:** Friendly name of the network device.
* **host:** Management IP address used to connect to the device.
* **device_type:** Netmiko platform identifier.

Update these example values to match your own lab environment.

## 6. Prerequisites

Before running the project, ensure that:

* Python is installed.
* Netmiko is installed.
* The Cisco routers are reachable over the management network.
* SSH is enabled and configured on the routers.
* Valid credentials are available.
* The inventory file contains the correct device information.

Install Netmiko using:

`python -m pip install netmiko`

## 7. How to Run the Project

1. Open the project folder in Visual Studio Code.

2. Open the integrated terminal.

3. Navigate to the project directory if necessary.

4. Run the script:

   `python network_audit.py`

5. Enter the requested username and password.

6. Allow the script to connect to each device and collect the command output.

7. Review the generated reports and audit summary.

## 8. Commands Executed

The script can be configured to execute commands such as:

* `show running-config | include ^hostname`
* `show ip interface brief`
* `show ip route`
* `show ip arp`
* `show running-config`

These commands collect device identity, interface status, routing information, ARP information, and running configuration.

The actual commands executed depend on the `command_list` defined in `network_audit.py`.

## 9. Output and Reports

### Individual Reports

The `reports/` directory contains separate text files for the commands executed on each device.

Each report includes the device name, command executed, and command output.

### Audit Summary

The `audit_summary.csv` file provides a consolidated view of the audit.

Its columns include:

* `device`
* `ip_address`
* `audit_status`
* `commands_successful`
* `commands_failed`

The summary helps identify devices that were audited successfully, devices with command failures, and devices that could not be reached.

## 10. Error Handling

The script uses Python exception handling to manage common connection problems, including:

* Authentication failures.
* Connection timeouts.
* Other unexpected errors.
* Individual command execution exceptions.

This helps the script continue processing other devices when a handled error occurs.

## 11. Security Considerations

* Do not commit real passwords to a public repository.
* Use authorized credentials and devices only.
* Restrict access to collected configuration reports.
* Review reports before sharing them, as running configurations may contain sensitive information.
* Use secure SSH configuration and trusted host-key verification appropriate to your environment.

## 12. Current Project Scope

This is a beginner-level network automation project focused on collecting operational information from Cisco routers.

The current version includes inventory-based device selection, SSH connectivity, command execution, report generation, summary reporting, and basic exception handling.

Additional features can be introduced as the project develops.

## 13. Possible Future Improvements

* Add structured logging and timestamps.
* Improve validation of command output.
* Add more detailed connection and command failure reporting.
* Export reports in additional formats.
* Add automated tests for successful and failed scenarios.
* Improve credential management and SSH host-key verification.

## 14. Learning Outcomes

Through this project, I practised Python file handling, CSV processing, lists and dictionaries, loops, functions and library usage, SSH-based network automation, exception handling, and automated report generation.
