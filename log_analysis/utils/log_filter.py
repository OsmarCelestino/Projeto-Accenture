from pydantic import BaseModel
from typing import Optional,Union
from datetime import datetime
from log_analysis.utils.helpers import Helper
from pydantic import BaseModel, validator

class LogFilter(BaseModel):
    start_date: Optional[Union[str, datetime]] = None
    end_date: Optional[Union[str, datetime]] = None
    message_contains: Optional[str] = None

    @validator('start_date', 'end_date', pre=True)
    def parse_date(cls, value):
            if isinstance(value, datetime):
                return value
            elif isinstance(value, str):
                return Helper.try_parse_date(value)
            raise ValueError("Input should be a valid string or datetime")