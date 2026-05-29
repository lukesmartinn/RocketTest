import urllib.request

print("--- METADATA DEEP SCAN ---")

# Zkusíme vlézt přímo do adresářů, které tam bývají
targets = [
    "latest/meta-data/hostname",
    "latest/meta-data/instance-id",
    "latest/meta-data/public-ipv4",
    "latest/meta-data/security-groups"
]

for path in targets:
    url = f"http://169.254.169.254/{path}"
    try:
        with urllib.request.urlopen(url, timeout=2) as response:
            print(f"PATH: {path} -> DATA: {response.read().decode()}")
    except Exception as e:
        print(f"PATH: {path} -> Nedostupné ({e})")

print("--- KONEC SCANU ---")