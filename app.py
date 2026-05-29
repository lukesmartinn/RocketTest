import os

print("--- ČTENÍ SERVICE ACCOUNT TOKENU ---")

token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"

if os.path.exists(token_path):
    with open(token_path, 'r') as f:
        token = f.read()
        # Vypíšeme jen začátek a konec, ať vidíš strukturu (je to JWT)
        print(f"TOKEN: {token[:20]}...[zkráceno]...{token[-20:]}")
        print(f"DÉLKA: {len(token)} znaků")
else:
    print("Token nenalezen.")

print("--- KONEC TESTU ---")