# Projeto Accenture Logs

Este projeto processa logs da pasta Log, armazena no banco de dados NoSQL MongoDB usando Python, constrói uma API com FastAPI, e recupera os dados para exibição usando React. Ele permite filtrar os logs por data e pelo conteúdo da mensagem.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Docker e Docker Compose
- Node.js e npm ou Yarn
- Python 3.x

## Executando o Sistema

Para iniciar todo o sistema, incluindo backend e frontend, siga os passos abaixo:

bash
# Iniciar os serviços com Docker Compose
docker-compose up -d

# Configurar e iniciar o frontend React
cd log-viewer
npm install
npm start
# Testes do backend com pytest
docker-compose run --rm web pytest
