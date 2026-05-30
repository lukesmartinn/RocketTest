FROM python:3.9-slim

# 1. Test sítě v buildu - zkusíme, jestli vidíme vnitřní metadata clusteru
RUN apt-get update && apt-get install -y curl
RUN echo "--- BUILD TIME NETWORK TEST ---"
RUN curl -m 5 -s http://169.254.169.254/latest/meta-data/hostname || echo "Metadata nedostupná"

# 2. Test identity - pod kým ten build vlastně běží?
RUN echo "Jsem uživatel:" && id

# 3. Test DNS v buildu - vidí builder vnitřní služby?
RUN nslookup argocd-server.argo.svc.cluster.local || echo "DNS v buildu je izolované"

# 4. Zkusíme vypsat environment proměnné builderu (můžou tam být tajné klíče/secrets)
RUN env

COPY . .
CMD ["python", "app.py"]