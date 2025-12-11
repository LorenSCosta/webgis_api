# Dockerfile para FastAPI Backend
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código
COPY . .

# Expõe porta do FastAPI
EXPOSE 8000

# Comando para rodar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
