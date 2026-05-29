import os

print("--- SYSTEM USER CHECK ---")
try:
    with open('/etc/passwd', 'r') as f:
        users = f.readlines()
        print(f"Našel jsem {len(users)} uživatelů v systému.")
        # Vypíšeme jen pár řádků, ať vidíme, jestli jsou tam i lidi zvenku
        for user in users[:10]:
            print(user.strip())
except Exception as e:
    print(f"Nemůžu číst /etc/passwd: {e}")