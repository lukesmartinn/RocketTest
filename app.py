import sys
import datetime
import os

print("--- START JEDNODUCHÉHO TESTU ---")

# Vypíšeme aktuální čas
now = datetime.datetime.now()
print(f"Čas spuštění: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Vypíšeme verzi Pythonu
print(f"Verze Pythonu: {sys.version}")

# Zkusíme vypsat uživatele, pod kterým to běží
try:
    user = os.getlogin()
except:
    user = "neznámý (pravděpodobně root v kontejneru)"
print(f"Aplikace běží pod uživatelem: {user}")

print("\nZpráva pro tebe:")
print("Všechno šlape, text se vypisuje správně. GJ!")

print("--- KONEC TESTU ---")