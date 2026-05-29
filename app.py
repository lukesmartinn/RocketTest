import os

print("--- SERVICE ACCOUNT TOKEN CHECK ---")

token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"
namespace_path = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"

if os.path.exists(token_path):
    print("!!! NAŠEL JSEM SERVICE ACCOUNT TOKEN !!!")
    with open(namespace_path, 'r') as f:
        print(f"Můj namespace: {f.read()}")
    
    # Zkusíme, jestli se s tím tokenem dá mluvit s API (přes curl/urllib)
    print("Zkouším komunikaci s K8s API pomocí tokenu...")
    # (Tady nebudeme vypisovat celý token do logu, to by byl moc velký leak)
    print("Token je přítomen a čitelný.")
else:
    print("Service account token nenalezen (správně izolováno).")

print("--- KONEC TESTU ---")