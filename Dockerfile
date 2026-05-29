FROM python:3.11-slim
WORKDIR /app
COPY app.py .
# Vypnutí bufferingu, aby logy tekly do platformy okamžitě
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]