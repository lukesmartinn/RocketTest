import os

print("--- PRŮZKUM SOUBORŮ ---")

# Zkusíme se podívat, jestli vidíme seznam všech uživatelů v systému
try:
    with open('/etc/passwd', 'r') as f:
        # Vypíšeme jen první dva řádky, ať to není kilometr dlouhý
        obsah = f.readlines()
        print("Můžu číst /etc/passwd!")
        print(f"Začátek souboru: {obsah[:2]}")
except Exception as e:
    print(f"Přístup k /etc/passwd zamítnut: {e}")

# Zkusíme, jestli vidíme, jaké další disky jsou připojené
try:
    with open('/proc/mounts', 'r') as f:
        print("Můžu číst /proc/mounts!")
except Exception as e:
    print(f"Přístup k /proc/mounts zamítnut: {e}")

print("--- KONEC PRŮZKUMU ---")