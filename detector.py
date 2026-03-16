from collections import defaultdict

def detect_port_scan(traffic):

    scans = defaultdict(set)

    for src, dst in traffic:

        scans[src].add(dst)

    suspicious = []

    for ip in scans:

        if len(scans[ip]) > 10:
            suspicious.append(ip)

    return suspicious


def detect_bruteforce(traffic):

    attempts = defaultdict(int)

    for src, dst in traffic:

        attempts[src] += 1

    attackers = []

    for ip in attempts:

        if attempts[ip] > 50:
            attackers.append(ip)

    return attackers