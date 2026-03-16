import streamlit as st
from analyzer import read_pcap
from detector import detect_port_scan, detect_bruteforce

st.title("SOC Detection Lab")

file = st.file_uploader("Upload PCAP", type="pcap")

if file:

    traffic = read_pcap(file)

    port_scans = detect_port_scan(traffic)

    bruteforce = detect_bruteforce(traffic)

    st.subheader("Detected Port Scans")
    st.write(port_scans)

    st.subheader("Detected Brute Force")
    st.write(bruteforce)