try:
    with open('build_scan.txt', 'r') as f:
        vysledek = f.read()
        print(f"--- VÝSLEDEK SKENU Z BUILD TIMU: {vysledek} ---")
except:
    print("Soubor build_scan.txt nenalezen.")