import streamlit as st
import nmap
import pandas as pd

st.title("Mini SOC Network Scanner")

network = st.text_input("Enter Network Range (example: 192.168.1.0/24)")

if st.button("Start Scan"):

    scanner = nmap.PortScanner()

    st.write("Scanning network...")

    scanner.scan(hosts=network, arguments="-O -sV")

    results = []

    for host in scanner.all_hosts():

        ip = host
        state = scanner[host].state()

        os_name = "Unknown"

        if "osmatch" in scanner[host] and len(scanner[host]["osmatch"]) > 0:
            os_name = scanner[host]["osmatch"][0]["name"]

        open_ports = []

        for proto in scanner[host].all_protocols():

            for port in scanner[host][proto]:

                if scanner[host][proto][port]["state"] == "open":
                    service = scanner[host][proto][port]["name"]
                    open_ports.append(f"{port} ({service})")

        results.append({
            "IP": ip,
            "State": state,
            "OS": os_name,
            "Open Ports": ", ".join(open_ports)
        })

    df = pd.DataFrame(results)

    st.subheader("Discovered Devices")
    st.dataframe(df)

    st.bar_chart(df["IP"].value_counts())