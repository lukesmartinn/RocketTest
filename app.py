import socket
import os

print("--- START NETWORK SCAN ---")

# IP adresa Kubernetes brány z tvého logu
target_ip = "10.96.0.1"
ports = [443, 80, 2379, 6443]

for port in ports:
    # Opravený řádek:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"!!! NAŠEL JSEM OTEVŘENÝ PORT {port} na {target_ip} !!!")
    else:
        print(f"Port {port} na {target_ip} je zavřený/blokovaný.")
    s.close()

print("--- SCAN KONEC ---")