import pytest
from datetime import datetime
from log_analysis.routes.log_routes import get_logs
from ..config.db_config import DatabaseConnector
from mongoengine import connect, disconnect
from log_analysis.models.log_record import LogRecord
from ..utils.log_filter import LogFilter

# Mock da função is_connected para retornar sempre True
@pytest.fixture
def mock_is_connected(monkeypatch):
    def mock_return(*args, **kwargs):
        return True
    monkeypatch.setattr('log_analysis.config.db_config.DatabaseConnector.is_connected', mock_return)

# Configuração do banco de dados de teste
@pytest.fixture(scope="module")
def mock_db():
    db_name = 'security_logs_test'
    db_host = 'mongo'
    db_port = 27017

    # Estabelecendo a conexão com o banco de dados de teste
    connect(db=db_name, host=db_host, port=db_port, alias='default')

    # Inserindo dados de teste no banco de dados
    LogRecord.objects.delete()  # Limpa dados existentes
   # Adicione os valores faltantes para 'product' e 'id_code'
    LogRecord.objects.create(
        ip="123.45.67.89", 
        date=datetime(2022, 1, 15), 
        additional_message="Erro encontrado", 
        activity_description="Teste de sistema",
        product="Nome do Produto",  # Exemplo de valor para o campo 'product'
        id_code="12345"  # Exemplo de valor para o campo 'id_code'
    )

    LogRecord.objects.create(
        ip="98.76.54.32", 
        date=datetime(2022, 3, 22), 
        additional_message="Tudo funcionando", 
        activity_description="Revisão de logs",
        product="Nome do Produto",  # Exemplo de valor para o campo 'product'
        id_code="67890"  # Exemplo de valor para o campo 'id_code'
    )

    yield  # Isso permite que os testes sejam executados

    # Desconectando e limpando o banco de dados após os testes
    disconnect(alias='test_db')


# Teste com filtro válido
def test_get_logs_with_valid_filter(mock_db, mock_is_connected):
    filter_obj = LogFilter(start_date=datetime(2022, 1, 1), end_date=datetime(2022, 12, 31), message_contains="Erro")
    results = get_logs(filter_obj)
    assert len(results) > 0
    assert any("Erro encontrado" in log['additional_message'] for log in results)

# Teste sem filtro
def test_get_logs_with_no_filter(mock_db, mock_is_connected):
    results = get_logs(None)
    assert len(results) == 2

# Teste com filtro de data que não retorna resultados
def test_get_logs_with_date_filter_no_results(mock_db, mock_is_connected):
    filter_obj = LogFilter(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31))
    results = get_logs(filter_obj)
    assert len(results) == 0

# Teste com filtro de mensagem que não retorna resultados
def test_get_logs_with_message_filter_no_results(mock_db, mock_is_connected):
    filter_obj = LogFilter(message_contains="Inexistente")
    results = get_logs(filter_obj)
    assert len(results) == 0
