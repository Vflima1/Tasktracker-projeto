# Base leve do sistema com Python 3.11
FROM python:3.11-slim

# Pasta central de operações dentro do container
WORKDIR /app

# Saída imediata no terminal e suporte a acentos (UTF-8)
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

# Copia o código local para dentro do container
COPY src/ /app/src/

# Comando que dispara a execução da aplicação
CMD ["python", "src/main.py"]
