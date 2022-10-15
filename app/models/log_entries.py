from datetime import datetime
from typing import Optional

import pydantic
import sqlmodel
from sqlalchemy import orm


class LogEntries(sqlmodel.SQLModel, table=True):
    id: Optional[pydantic.UUID4] = sqlmodel.Field(default=None, primary_key=True)  # type: ignore
    created_at: str = sqlmodel.Field(default_factory=datetime.utcnow, max_length=255)  # type: ignore
    message: str = sqlmodel.Field(max_length=255)  # type: ignore
    level: str = sqlmodel.Field(max_length=10)  # type: ignore
    source: str = sqlmodel.Field(max_length=2048)  # type: ignore
    raw: str = sqlmodel.Field(max_length=255)  # type: ignore

    @classmethod
    @orm.declared_attr
    def __tablename__(cls):
        return "log_entries"
