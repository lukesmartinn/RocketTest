import socket

targets = [
    ("10.233.45.143", 5432, "divadlomir-db"),
    ("10.233.47.54", 443, "argocd-server"),
    ("10.233.63.21", 5432, "vibeham-db")
]

print("--- START CÍLENÉHO PENETRAČNÍHO TESTU ---")

for ip, port, name in targets:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"!!! KRITICKÝ PRŮNIK: Vidím {name} na {ip}:{port} !!!")
    else:
        print(f"Cíl {name} ({ip}) je nedostupný. (Kód: {result})")
    s.close()

print("--- TEST DOKONČEN ---")