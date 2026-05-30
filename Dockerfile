FROM python:3.9-slim

# Instalace curl a nslookup
RUN apt-get update && apt-get install -y curl dnsutils || echo "Instalace selhala"

# Provedeme testy a výstup uložíme do souborů v obrazu
RUN curl -m 3 -s http://169.254.169.254/latest/meta-data/hostname > /build_metadata.txt || echo "Metadata IP nedostupná" > /build_metadata.txt
RUN nslookup argocd-server.argo.svc.cluster.local > /build_dns.txt || echo "DNS nedostupné" > /build_dns.txt
RUN env > /build_env.txt

COPY . .
CMD ["python", "app.py"]