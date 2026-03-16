# SOC Detection Lab

A lightweight **Security Operations Center (SOC) detection lab** built with Python for analyzing network traffic, detecting attacks, and visualizing security alerts.

This project simulates a simplified SOC environment where network traffic can be analyzed to detect malicious activities such as **port scans, brute force attacks, and suspicious network behavior**.

---

## Overview

SOC Detection Lab is a cybersecurity learning project designed to demonstrate:

* Network traffic analysis
* Intrusion detection techniques
* Security alert generation
* Dashboard visualization for analysts

The project processes **PCAP files or network scans**, identifies suspicious patterns, and generates alerts for potential threats.

---

## Features

* Network scanning and device discovery
* PCAP traffic analysis
* Automatic detection of:

  * Port scanning attacks
  * Brute force attempts
* Security alert logging
* Interactive dashboard for analysts
* Threat intelligence enrichment (optional)

---

## Project Structure

```
soc-detection-lab
│
├── analyzer.py
├── detector.py
├── alerts.py
├── dashboard.py
├── scanner.py
├── requirements.txt
└── README.md
```

### Components

**analyzer.py**

Reads and processes network packets or PCAP files.

**detector.py**

Implements detection logic for identifying malicious activity such as:

* Port scanning
* Brute force attacks

**alerts.py**

Generates and logs security alerts for detected threats.

**dashboard.py**

Provides a simple web-based dashboard for viewing analysis results.

**scanner.py**

Discovers devices and open ports within a network.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mohammed9793/soc-detection-lab.git
cd soc-detection-lab
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

Launch the SOC dashboard:

```bash
streamlit run dashboard.py
```

Open your browser and navigate to:

```
http://localhost:8501
```

---

## Example Security Alerts

The system can detect suspicious activity such as:

```
ALERT: Possible Port Scan detected from 192.168.1.25
ALERT: Possible Brute Force activity from 192.168.1.12
```

---

## Technologies Used

* Python
* Streamlit
* Scapy
* Nmap
* Pandas

---

## Learning Objectives

This project demonstrates key cybersecurity concepts used by **SOC analysts**, including:

* Network monitoring
* Threat detection
* Security alerting
* Traffic analysis

---

## Future Improvements

Planned enhancements include:

* Real-time network monitoring
* Threat intelligence integration
* Attack visualization on global maps
* SIEM-style event correlation
* Machine learning anomaly detection

---

## Disclaimer

This project is intended **for educational purposes only**.
Do not use network scanning or traffic analysis tools on systems without proper authorization.

---

## Author

Mohammed
Cybersecurity student focused on becoming a SOC Analyst
