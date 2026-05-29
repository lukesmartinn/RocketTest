import socket

# Seznam vnitřních názvů, které jsme vytáhli z tvého kubectl výpisu
# Formát v K8s je: název-služby.namespace.svc.cluster.local
internal_names = [
    "kubernetes.default.svc.cluster.local",
    "divadlomir-db.divadlomir-osykora.svc.cluster.local",
    "argocd-server.argocd.svc.cluster.local",
    "vibeham-db.vibeham.svc.cluster.local",
    "postgres.vibeham.svc.cluster.local",
    "mirplay-db.divadlomir-osykora.svc.cluster.local"
]

print("--- START DNS RECON SCAN ---")

for name in internal_names:
    try:
        # Zkusíme přeložit název na IP adresu
        ip = socket.gethostbyname(name)
        print(f"!!! LEAK: Přeložil jsem {name} na IP {ip} !!!")
    except socket.gaierror:
        # Tohle je správné chování - aplikace by neměla vědět, že tyhle názvy existují
        print(f"Název {name} je (správně) neznámý.")
    except Exception as e:
        print(f"Chyba u {name}: {e}")

print("--- SCAN KONEC ---")