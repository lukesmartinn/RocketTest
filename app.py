import os
try:
    # Hledáme soubor v kořenovém adresáři, kam jsme ho v Dockerfilu uložili
    if os.path.exists('/build_scan.txt'):
        with open('/build_scan.txt', 'r') as f:
            print(f"--- VÝSLEDEK SKENU Z BUILD TIMU: {f.read()} ---")
    else:
        print("Soubor /build_scan.txt na disku fakt není.")
except Exception as e:
    print(f"Chyba při čtení: {e}")