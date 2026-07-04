import socket

def scan_ports(ip, ports):
    print(f"Scanning {ip}...\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: closed or filtered")

        sock.close()

if __name__ == "__main__":
    target_ip = "192.168.1.100"  # Replace with your target IP
    ports = [22, 80, 443, 3389]

    scan_ports(target_ip, ports)

#//scan a range//
import socket

target_ip = "192.168.1.100"

for port in range(1, 1025):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.2)

        if sock.connect_ex((target_ip, port)) == 0:
            print(f"Port {port} is open")

#//scan multiple ips//

import socket


ips = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
]

ports = [22, 80, 443]

for ip in ips:
    print(f"\nScanning {ip}")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.3)
            if sock.connect_ex((ip, port)) == 0:
                print(f"{port}: OPEN")

# //find subdomain//
import requests

def find_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=45)
        response.raise_for_status()

        data = response.json()

        subdomains = set()

        for entry in data:
            names = entry.get("name_value", "").split("\n")
            for name in names:
                if name.endswith(domain):
                    subdomains.add(name.strip())

        return sorted(subdomains)

    except requests.RequestException as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    domain = input("Enter a domain: ").strip()

    results = find_subdomains(domain)

    print(f"\nFound {len(results)} unique subdomains:\n")
    for subdomain in results:
        print(subdomain)

