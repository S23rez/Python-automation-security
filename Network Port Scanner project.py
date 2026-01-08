import socket
import threading
import ipaddress
import logging
from queue import Queue

# -----------------------------
# Logging configuration
# -----------------------------
logging.basicConfig(filename="scan_log.txt",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")


# -----------------------------
# Port scanning function
# -----------------------------
def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    try:
        result = scanner.connect_ex((ip, port))
        if result == 0:
            print(f"[OPEN] {ip}:{port}")
            logging.info(f"[OPEN] {ip}:{port}")
        else:
            logging.info(f"[CLOSED] {ip}:{port}")
    except Exception as e:
        logging.info(f"[ERROR] {ip}:{port} - {e}")
    finally:
        scanner.close()


# -----------------------------
# Worker for multi-threading
# -----------------------------
def worker():
    while not queue.empty():
        ip, port = queue.get()
        scan_port(ip, port)
        queue.task_done()


# -----------------------------
# Get IP range
# -----------------------------
def get_ip_list(ip_input):
    try:
        if "/" in ip_input:
            return [str(ip) for ip in ipaddress.ip_network(ip_input, strict=False).hosts()]
        elif "-" in ip_input:
            # Handle ranges across different octets
            start_ip, end_ip = ip_input.split("-")
            # This is a bit complex, but simple version:
            # Assume range is only last octet for now but add a check
            return [f"{'.'.join(start_ip.split('.')[:-1])}.{i}" for i in range(int(start_ip.split('.')[-1]), int(end_ip)+1)]
        else:
            return [str(ipaddress.ip_address(ip_input))]
    except Exception as e:
        print(f"Error parsing IP: {e}")
        return []


# -----------------------------
# Get port range
# -----------------------------
def get_port_list(port_input):
    # Common services shortcut
    services = {
        "http": 80,
        "https": 443,
        "ssh": 22,
        "ftp": 21
    }

    if port_input.lower() in services:
        return [services[port_input.lower()]]

    if "-" in port_input:
        start, end = port_input.split("-")
        return list(range(int(start), int(end) + 1))

    return [int(port_input)]


# -----------------------------
# MAIN PROGRAM
# -----------------------------
queue = Queue()

print("=== PYTHON NETWORK PORT SCANNER ===")
ip_input = input("Enter IP (single), Range (192.168.1.1-20) or Subnet (192.168.1.0/24): ")
port_input = input("Enter single port, range (20-80), or service (http, ssh, ftp): ")

ip_list = get_ip_list(ip_input)
port_list = get_port_list(port_input)

print(f"\nScanning {len(ip_list)} host(s) on {len(port_list)} port(s)...\n")

# Load tasks into queue
for ip in ip_list:
    for port in port_list:
        queue.put((ip, port))

# Start multi-threading
threads = []
for _ in range(100):  # 100 threads
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

queue.join()

print("\nScan completed. Results saved to scan_log.txt.")