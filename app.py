import urllib.request

print("--- START METADATA ROOT SCAN ---")
# Zkusíme jen základní adresu bez podadresářů
url = "http://169.254.169.254/"

try:
    with urllib.request.urlopen(url, timeout=2) as response:
        print("!!! SERVER ODPOVĚDĚL !!!")
        print(f"DOSTUPNÉ CESTY: {response.read().decode()}")
except Exception as e:
    print(f"Chyba: {e}")

print("--- KONEC TESTU ---")