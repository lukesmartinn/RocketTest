import urllib.request

print("--- START METADATA TEST ---")

# Tohle je standardní magická IP v cloudech (AWS, GCP, Azure, OpenStack)
url = "http://169.254.169.254/latest/meta-data/"

try:
    # Zkusíme tam prostě klepnout a přečíst odpověď
    with urllib.request.urlopen(url, timeout=2) as response:
        print("!!! NAŠEL JSEM CLOUD METADATA !!!")
        print(f"ODPOVĚĎ: {response.read().decode()}")
except Exception as e:
    print(f"Metadata nedostupná: {e}")

print("--- KONEC TESTU ---")