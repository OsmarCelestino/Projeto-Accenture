import os
from datetime import datetime
from log_analysis.models.log_record import LogRecord
from fastapi import HTTPException, status

def process_log_file(path=None):
  
    if path is None:
        path = "/app/Logs"

    try:

        if os.path.isdir(path):
            
            for filename in os.listdir(path):
                full_path = os.path.join(path, filename)
                if os.path.isfile(full_path):
                    process_file(full_path)
        elif os.path.isfile(path):

            process_file(path)
        else:
            print(f"Caminho fornecido não é um arquivo nem um diretório: {path}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Caminho inválido fornecido.")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno ao processar logs.")

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) != 8:
                    print(f"Linha mal formatada: {line}")
                    continue
                try:
                    log_entry = LogRecord(
                        ip=parts[0],
                        date=datetime.strptime(parts[1], '%d-%b-%Y'),
                        product=parts[3],
                        version=parts[4],
                        id_code=parts[5],
                        activity_description=parts[6],
                        additional_message=parts[7]
                    )
                    log_entry.save()
                except Exception as e:
                    print(f"Erro ao processar a linha: {line}. Erro: {e}")
    except IOError as e:
        print(f"Erro ao abrir o arquivo: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao processar arquivo de log.")
