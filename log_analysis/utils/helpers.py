from datetime import datetime
from bson import ObjectId


class Helper:

    @staticmethod
    def try_parse_date(date_input):
        if date_input:
            if isinstance(date_input, datetime):
                return date_input
            
            date_input = date_input.rstrip("Z")
            
            for fmt in ("%d/%m/%Y", "%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
                try:
                    return datetime.strptime(date_input, fmt)
                except ValueError:
                    continue

            raise ValueError("Formato de data inválido.")

        return None  

    @staticmethod
    def convert_objectid_to_string(data):
        if isinstance(data, list):
            return [Helper.convert_objectid_to_string(item) for item in data]
        if isinstance(data, dict):
            return {k: (str(v) if isinstance(v, ObjectId) else Helper.convert_objectid_to_string(v)) for k, v in data.items()}
        return data
