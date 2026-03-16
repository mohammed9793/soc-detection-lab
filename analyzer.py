from scapy.all import rdpcap

def read_pcap(file):

    packets = rdpcap(file)

    traffic = []

    for pkt in packets:

        if pkt.haslayer("IP"):

            src = pkt["IP"].src
            dst = pkt["IP"].dst

            traffic.append((src, dst))

    return traffic