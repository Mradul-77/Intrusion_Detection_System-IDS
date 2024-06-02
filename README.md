# Intrusion Detection System(IDS) on Windows:
'Intrusion Detection System(IDS) on Windows' is a project which serves the security technology designed to detect malicious activities within a computer system or network.
## Overview:
It comprises interconnected components—client-side, server-side operations, and an analyser module. 
Client-Side Script: Engages in extensive data gathering, meticulously extracting a spectrum of system details and metrics.

Server-Side Script: Functions as a central repository, responsibly handling incoming data from multiple clients. Conducts preliminary data processing before directing information streams to the analyser for in-depth scrutiny.

Analyzer: Serves as the core unit, meticulously dissecting incoming data, searching for anomalies or potential security breaches.

### 008-SERVER.py:
Sets up the host computer as a server ready to take connections from clients. After receiving the client’s data, it stores them as ‘.xyz’ files.

### 008-CLIENT.py:
Retrieves data about the host’s system information, processes and connections, connects to the server and sends the data collected back to the server.

### 008-ANALYZER_1.py:
Converts the stored ‘.xyz’ files to ‘.csv’ files.

### 008-ANALYZER_2.py:
Checks the .csv files for and malicious activities in the client’s 	system based on the Blacklist files provided. It generates an alert file accordingly. Then creates a new folder and moves all the essential files into it.

## Information about .csv files:
### PROINFO.csv:
It contains details of all the ongoing processes on the client side. It has parameters like PROCESSID, PROCESSNAME, STATUS and START TIME.
### NETINFO.csv:
It contains details of all the networks to which the client is connected to. It has parameters like PROCESSID, STATUS, LOCALIP, LOCALPORT, REMOTEIP and REMOTEPORT.
### PROCESS_BLACKLIST.csv:
It contains the information of the processes that can be potentially malicious and harmful for the system. It has the record of the process-name and the danger-level of the blacklisted processes.
### IP_BLACKLIST.csv:
It contains the information about the IPs that can be malicious or potentially hazardous for the client’s system. It has the record of the IP addresses and the danger-level of the blacklisted IPs.
### SYS_INFO:
It doesn't have any important role in the project. It just contains information about the user's(server) PC/device and its configuration, for future use.

## Role of the Analyzer modules:
The most important job of the Analyzer Script is to create the PROALERT and IPALERT files.
The <I> PROALERT file contains information about the malicious processes, their process-id, their danger level and where to find it in the PROINFO file for more information.
The <I> IPALERT file contains information about the unsafe sites and computers to which the client is connected to. It contains the remote-ip, remote-port and process-id of the processes which are connected to these sites and also where to find them in the NETINFO file.
The user on the server side can now use this information to figure out whether or not the client’s system may be compromised and then take the necessary actions. 

