import nmap

def scan_target(target):
    scanner = nmap.PortScanner()

    print(f"Scanning {target}...")

    scanner.scan(target, "1-1024")

    for host in scanner.all_hosts():
        print("Host:", host)
        print("State:", scanner[host].state())

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()

            for port in ports:
                state = scanner[host][proto][port]["state"]
                print(f"Port {port}: {state}")

if __name__ == "__main__":
    target = input("Enter IP to scan: ")
    scan_target(target)