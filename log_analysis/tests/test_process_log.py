import pytest
from log_analysis.services.process_log_file import process_log_file
from unittest.mock import mock_open
from fastapi import HTTPException, status
from ..models.log_record import LogRecord
from mongoengine import connect, disconnect

valid_log_file_path = "/app/Logs/AccessLogs (1).txt"
mocked_file_content = "192.168.0.1;01-Jan-2022;INFO;ProductX;1.0;ID123;Activity description;Additional message"

@pytest.fixture(scope='module')
def setup_db_test():
    connect('security_logs_test', host='mongo', port=27017, alias='default')
    yield
    disconnect()

@pytest.fixture
def mock_log_record_save(mocker):
    mocker.patch.object(LogRecord, 'save')

# Teste para um caminho de arquivo válido
def test_process_log_file_single_file(mock_log_record_save, mocker, setup_db_test):
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('builtins.open', mock_open(read_data=mocked_file_content))
    process_log_file(valid_log_file_path)

# Teste para erro ao abrir o arquivo
def test_process_log_file_io_error(mocker):
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('builtins.open', side_effect=IOError("Erro ao abrir"))
    with pytest.raises(HTTPException) as excinfo:
        process_log_file(valid_log_file_path)
    assert excinfo.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

# Teste para verificar se o processamento de diretório está correto
def test_process_log_file_directory(mock_log_record_save, mocker):
    mocker.patch('os.listdir', return_value=['AccessLogs (1).txt'])
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.path.isfile', side_effect=lambda x: x.endswith('.txt'))
    mocker.patch('builtins.open', mock_open(read_data=mocked_file_content))
    process_log_file("/app/Logs")
