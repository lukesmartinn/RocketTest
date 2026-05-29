import urllib.request
import json
import ssl

print("--- CO VŠE VLASTNĚ MŮŽU? ---")

# Cesta k tokenu, který jsi našel
token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"
api_url = "https://kubernetes.default.svc/api/v1/namespaces/default/pods"

try:
    with open(token_path, 'r') as f:
        token = f.read().strip()

    # Musíme ignorovat SSL certifikát, protože je vnitřní
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(api_url)
    req.add_header('Authorization', f'Bearer {token}')

    with urllib.request.urlopen(req, context=ctx, timeout=2) as response:
        print("!!! TY KRÁSO: API mě pustilo k seznamu podů !!!")
        data = json.loads(response.read().decode())
        print(f"Vidím {len(data.get('items', []))} běžících podů v defaultu.")
except Exception as e:
    print(f"API mě nepustilo dál (Kód: {e})")

print("--- KONEC PRŮZKUMU ---")