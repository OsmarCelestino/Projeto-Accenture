from fastapi import APIRouter
from ..services.process_log_file import process_log_file
from fastapi import HTTPException, status
from ..utils.log_filter import LogFilter
from typing import Optional
from log_analysis.utils.helpers import *
from ..config.db_config import DatabaseConnector
from ..services.log_service import LogService
from mongoengine import get_connection
from pymongo.errors import OperationFailure


router = APIRouter()


@router.post("/logs/process-logs/")
def process_logs():
    if not DatabaseConnector.is_connected():
        print("Não conectado ao banco de dados.")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Sem conexão com o banco de dados.")
    try:
        process_log_file()
        return {"message": "Logs processados e organizados com sucesso."}
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/database/clear")
def clear_database():
    try:
        db_name = "security_logs"  # substitua pelo nome do seu banco de dados
        # Usando a conexão existente
        db_client = get_connection()
        db_client.drop_database(db_name)
        return {"message": "Banco de dados limpo com sucesso"}
    except OperationFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Falha ao limpar o banco de dados: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao tentar limpar o banco de dados: {e}"
        )

@router.post("/logs/get/")
def get_logs(filter: Optional[LogFilter] = None):
    if not DatabaseConnector.is_connected():
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Sem conexão com o banco de dados.")

    try:
        return LogService.get_filtered_logs(filter)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Ocorreu um erro ao processar a solicitação: {e}"
        )