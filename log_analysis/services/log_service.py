# log_service.p
from typing import List, Optional
from mongoengine.queryset.visitor import Q
from ..utils.helpers import Helper
from ..models.log_record import LogRecord
from ..utils.log_filter import LogFilter
from functools import reduce

class LogService:
    @staticmethod
    def get_filtered_logs(filter: Optional[LogFilter] = None) -> List[dict]:
        queries = []

        if filter and filter.message_contains:
            regex_filter = f".*{filter.message_contains.strip()}.*"
            message_query = Q(additional_message__iregex=regex_filter)
            queries.append(message_query)

        if filter and filter.start_date:
            parsed_start_date = Helper.try_parse_date(filter.start_date)
            if parsed_start_date:
                start_date_query = Q(date__gte=parsed_start_date)
                queries.append(start_date_query)

        if filter and filter.end_date:
            parsed_end_date = Helper.try_parse_date(filter.end_date)
            if parsed_end_date:
                end_date_query = Q(date__lte=parsed_end_date)
                queries.append(end_date_query)

        final_query = reduce(lambda x, y: x & y, queries) if queries else None
        filtered_logs = LogRecord.objects(final_query) if final_query is not None else LogRecord.objects()
        
        return [Helper.convert_objectid_to_string(log.to_mongo().to_dict()) for log in filtered_logs]
