import os

print("--- KONTROLA NASTAVENÍ (ENVVARS) ---")

# Vypíše všechno, co platforma o sobě a aplikaci prozradí
for k, v in os.environ.items():
    # Vypíšeme jen začátek hodnoty, ať je to bezpečný
    print(f"KLÍČ: {k} | HODNOTA: {v[:10]}...")

print("--- KONEC KONTROLY ---")