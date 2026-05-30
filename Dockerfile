FROM python:3.9-slim

# Instalace nástrojů (pokud chybí)
RUN apt-get update && apt-get install -y curl dnsutils || echo "Instalace selhala"

RUN echo "--- START BUILD RECON ---"

# Test metadat (s ignorováním chyby - || true)
RUN curl -m 3 -v http://169.254.169.254/latest/meta-data/hostname || echo "Metadata IP nedostupná"

# Test DNS (s ignorováním chyby)
RUN nslookup argocd-server.argo.svc.cluster.local || echo "Vnitřní DNS nedostupné z buildu"

# Výpis env - tohle projde vždycky
RUN env > /build_env.txt && echo "Env vars uloženy"

RUN echo "--- END BUILD RECON ---"

COPY . .
CMD ["python", "app.py"]