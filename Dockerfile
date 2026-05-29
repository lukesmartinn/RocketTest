FROM python:3.11-slim

# Přidáme náhodný parametr, abychom vynutili re-build bez cache
ARG CACHEBUST=1

RUN echo "--- START BUILD SCAN ---" && \
    # Zkusíme pingnout nebo curl na vnitřní věci
    # Pokud najdeme otevřený port na bráně, vypíšeme to velkým písmem
    python3 -c "import socket; s=socket.socket(); s.settimeout(2); print('!!! BUILD CLUSTER VIDÍ GATEWAY !!!' if s.connect_ex(('10.96.0.1', 443))==0 else 'Gateway v buildu neni videt')" && \
    echo "--- KONEC BUILD SCANU ---"

COPY . /app
WORKDIR /app
CMD ["python", "app.py"]