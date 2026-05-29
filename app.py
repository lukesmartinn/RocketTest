import socket

# Porty pro Kuma/Kong/Gateway metriky a admin
gateway_ports = [5681, 5683, 8001, 8444, 9091]

print("--- GATEWAY RECON ---")
for port in gateway_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex(("10.96.0.1", port)) == 0:
        print(f"!!! NAŠEL JSEM GATEWAY PORT {port} !!!")
    s.close()