import socket
import os

print("--- START NETWORK SCAN ---")

# Zkusíme se připojit na vnitřní IP Kubernetes, kterou jsi našel v logu
target_ip = "10.96.0.1"
ports = [443, 80, 2379, 6443] # Běžné porty pro ovládání sítě

for port in ports:
    s = socket.socket(socket.socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Nechceme čekat věčně
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"!!! NAŠEL JSEM OTEVŘENÝ PORT {port} na {target_ip} !!!")
    else:
        print(f"Port {port} na {target_ip} je zavřený nebo blokovaný.")
    s.close()

print("--- SCAN KONEC ---")