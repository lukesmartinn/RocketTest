import random
import time

# Seznam náhodných hlášek pro odlehčení
quotes = [
    "Kóduj, jako by ten, kdo ho po tobě bude spravovat, byl násilnický psychopat, který ví, kde bydlíš.",
    "Hardware je to, do čeho můžeš kopnout, když přestane fungovat software.",
    "Předpoklad je matka všech průšvihů.",
    "Nefunguje to? Zkusil jsi to vypnout a znova zapnout?",
    "V mém počítači to fungovalo normálně..."
]

print("="*40)
print("   VÍTEJ V GENERÁTORU NÁHODNÉHO CHAOSU   ")
print("="*40)

# Simulace nějaké "práce"
for i in range(1, 4):
    print(f"Probíhá hloubková analýza vesmíru... {i*33}%")
    time.sleep(0.5)

print("\nVýsledek dnešní věštby:")
print(f">>> {random.choice(quotes)} <<<")

print("\n" + "="*40)
print("         TEST ÚSPĚŠNĚ DOKONČEN          ")
print("="*40)