import os

def read_build_file(name):
    print(f"--- VÝSLEDEK Z BUILDU: {name} ---")
    if os.path.exists(name):
        with open(name, 'r') as f:
            print(f.read())
    else:
        print("Soubor nenalezen.")

# Přečteme to, co jsme si v buildu připravili
read_build_file("/build_metadata.txt")
read_build_file("/build_dns.txt")
read_build_file("/build_env.txt")

print("--- RUNTIME IS READY ---")