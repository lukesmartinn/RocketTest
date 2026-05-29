import urllib.request

# Standardní porty pro Envoy / Kuma Sidecar administraci
proxy_targets = [
    ("http://127.0.0.1:15000/clusters", "Envoy Clusters"),
    ("http://127.0.0.1:15000/config_dump", "Envoy Config"),
    ("http://127.0.0.1:9901/stats", "Kuma Stats")
]

print("--- PROXY SIDECAR RECON ---")

for url, name in proxy_targets:
    try:
        with urllib.request.urlopen(url, timeout=2) as response:
            print(f"!!! NAŠEL JSEM {name} !!!")
            # Vypíšeme jen kousek, bývá to obří
            print(response.read().decode()[:500])
            print("-" * 20)
    except Exception as e:
        print(f"{name} na {url} nedostupné: {e}")

print("--- KONEC TESTU ---")