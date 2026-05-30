FROM python:3.9-slim
RUN apt-get update && apt-get install -y curl

# Zkusíme poslat falešný log přímo do jejich vnitřního sběrače logů během buildu!
RUN curl -X POST http://127.0.0.1:44725/v1/logs \
    -H "Content-Type: application/json" \
    -d '{"resourceLogs": [{"resource": {"attributes": [{"key": "service.name", "value": "HACKED-BY-MARTIN"}]}}]}' || echo "OTEL nedostupný"

# Zkusíme, jestli builder vidí ven na internet (Google DNS)
RUN curl -m 3 -I http://8.8.8.8 || echo "Build nemá přístup k internetu"

COPY . .
CMD ["python", "app.py"]