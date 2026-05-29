import socket

# Seznam věcí, co by v cloudu mohly běžet
targets = [
    "redis", "redis-master", "redis-slave", 
    "postgres", "postgresql", "mysql", "mariadb", 
    "mongodb", "rabbitmq", "valkey"
]

# Zkusíme i standardní namespaces
namespaces = ["default", "redis", "database", "infra"]

print("--- DEEP DNS RECON ---")

for target in targets:
    for ns in namespaces:
        fqdn = f"{target}.{ns}.svc.cluster.local"
        try:
            ip = socket.gethostbyname(fqdn)
            print(f"!!! NAŠEL JSEM SLUŽBU: {fqdn} -> {ip}")
            
            # Pokud to najde Redis, zkusíme rovnou port 6379
            if "redis" in target:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((ip, 6379)) == 0:
                    print(f"  [+] Port 6379 je OTEVŘENÝ na {ip}")
                s.close()
        except:
            continue

print("--- SCAN DOKONČEN ---")