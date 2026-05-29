import socket

print("--- SKENOVÁNÍ VNITŘNÍ SÍTĚ NA POSTGRES (5432) ---")

# Zkusíme projet širší rozsah vnitřní sítě
# Adresa 10.99.4.10 byla tvoje, tak zkusíme okolí
prefix = "10.99.4."
for i in range(1, 20):  # Zkusíme prvních 20 adres v tvém subnetu
    target = f"{prefix}{i}"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Rychlý sken
    result = s.connect_ex((target, 5432))
    if result == 0:
        print(f"!!! NAŠEL JSEM CIZÍ POSTGRES NA {target}:5432 !!!")
    s.close()

print("--- SKEN DOKONČEN ---")