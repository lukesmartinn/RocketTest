import socket

# Talos API standardně běží na 50000
target_ip = "169.254.169.254" # Nebo zkus tu IP, co ti vypadlo public-ipv4 předtím
port = 50000

print(f"--- TALOS API PROBE NA {port} ---")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
if s.connect_ex((target_ip, port)) == 0:
    print(f"!!! KRITICKÉ: Vidím TALOS API na portu {port} !!!")
else:
    print(f"Talos API port {port} je (správně) zavřený.")
s.close()