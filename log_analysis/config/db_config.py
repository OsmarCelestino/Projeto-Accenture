from mongoengine import connect
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError
from mongoengine.connection import get_connection

class DatabaseConnector:
    __db_name = "security_logs"
    __db_host = "mongo"
    __db_port = 27017

    @staticmethod
    def initialize_connection():
        try:
            
            db_client = connect(db=DatabaseConnector.__db_name, host=DatabaseConnector.__db_host, port=DatabaseConnector.__db_port)   
            db_client.server_info() 
            print(f"Conectado ao banco de dados {DatabaseConnector.__db_name} em {DatabaseConnector.__db_host}:{DatabaseConnector.__db_port}")
        except OperationFailure as e:
            print(f"Falha na operação do MongoDB: {e}")
            raise e
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise e

    @staticmethod
    def is_connected():
        try:
            get_connection()
            return True
        except ServerSelectionTimeoutError as e:
            print(f"Timeout ao tentar conectar ao banco de dados: {e}")
            return False
        except Exception as e:
            print(f"Erro ao verificar a conexão com o banco de dados: {e}")
            return False
