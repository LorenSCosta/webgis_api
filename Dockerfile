# Imagem base
FROM python:3.13-slim

# Define diretório de trabalho
WORKDIR /app

# Instala Poetry
RUN pip install --no-cache-dir poetry

# Copia arquivos de dependência
COPY pyproject.toml poetry.lock* /app/

# Configura Poetry e instala dependências sem criar virtualenv
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia o código fonte
COPY . /app

# Expõe porta
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
