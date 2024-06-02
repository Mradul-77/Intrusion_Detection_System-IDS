# Intrusion Detection System(IDS) on Windows:
'Intrusion Detection System(IDS) on Windows' is a project which serves the security technology designed to detect malicious activities within a computer system or network.
### Overview:
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


