from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import func
from typing_extensions import Annotated
import datetime


class Base(DeclarativeBase):
    pass


# NOTE: Not sure if this will work properly for all db implementations
timestamp = Annotated[
    datetime.datetime, mapped_column(nullable=False, server_default=func.UTC_TIMESTAMP)
]
