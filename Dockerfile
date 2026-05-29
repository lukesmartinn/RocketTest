# Použijeme nějaký základní image
FROM python:3.11-slim

# Nainstalujeme nmap (nástroj na skenování sítě) přímo během buildu
RUN apt-get update && apt-get install -y nmap

# Tady je ten "brotip" v praxi - skenujeme okolí během buildu
RUN echo "--- START BUILD-TIME NETWORK SCAN ---" && \
    # Zkusíme skenovat okolní adresy, jestli tam něco neuvidíme (třeba ten divadlomir)
    # Rozsah 10.0.0.0/16 je často používaný pro interní věci
    nmap -sn 10.96.0.0/24 || true && \
    echo "--- KONEC BUILD-TIME SCANU ---"

# Pak už klasika zbytek tvého Dockerfile...
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]