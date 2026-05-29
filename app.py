import urllib.request
import ssl

print("--- CURL TEST NA 10.96.0.1 ---")
context = ssl._create_unverified_context()

try:
    # Zkusíme zjistit verzi API serveru
    req = urllib.request.Request("https://10.96.0.1:443/version")
    with urllib.request.urlopen(req, context=context, timeout=2) as response:
        print(f"STATUS: {response.getcode()}")
        print(f"DATA: {response.read().decode()}")
except Exception as e:
    print(f"CHYBA: {e}")

print("--- KONEC TESTU ---")