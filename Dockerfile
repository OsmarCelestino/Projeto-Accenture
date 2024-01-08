# Usa uma imagem base do Python
FROM python:3.8

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos para o container
COPY . .

# Instala as dependências listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar a aplicação
CMD ["uvicorn", "log_analysis.main:app", "--host", "0.0.0.0", "--port", "80"]

