# Projeto Accenture Logs

Este projeto processa logs da pasta Log, armazena no banco de dados NoSQL MongoDB usando Python, constrói uma API com FastAPI, e recupera os dados para exibição usando React. Ele permite filtrar os logs por data e pelo conteúdo da mensagem.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Docker e Docker Compose

## Executando o Sistema

Para iniciar todo o sistema, incluindo backend e frontend, siga os passos abaixo:


# Iniciar os serviços com Docker Compose
docker-compose up ou docker-compose up -d

# Testes do backend com pytest
docker-compose run --rm api pytest

# Teste frontend React
npx cypress open


