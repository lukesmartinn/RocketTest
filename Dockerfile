FROM python:3.11-slim

# Tohle vynutí re-build, protože 'date' je pokaždé jiný
RUN date > /timestamp.txt

# Teď ten samotný sken
RUN python3 -c "import socket; s=socket.socket(); s.settimeout(2); res='ANO' if s.connect_ex(('10.96.0.1', 443))==0 else 'NE'; open('/build_scan.txt', 'w').write(res)" || true

COPY . /app
WORKDIR /app
CMD ["python", "app.py"]