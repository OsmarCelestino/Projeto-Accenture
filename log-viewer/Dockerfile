# Escolha a imagem do Node
FROM node:14

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências e instala as dependências
COPY log-viewer/package.json log-viewer/package-lock.json ./
RUN npm install

# Copia os arquivos do projeto
COPY . .

# Constrói a aplicação para produção
RUN npm run build

# Serve a aplicação usando um servidor HTTP simples
CMD ["npx", "serve", "-s", "build", "-l", "80"]
