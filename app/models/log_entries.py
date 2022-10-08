from datetime import datetime
from typing import Optional

import pydantic
import sqlmodel
from sqlalchemy import orm


class LogEntries(sqlmodel.SQLModel, table=True):
    id: Optional[pydantic.UUID4] = sqlmodel.Field(default=None, primary_key=True)  # type: ignore
    created_at: datetime = sqlmodel.Field(  # type: ignore
        default_factory=datetime.utcnow
    )
    message: str
    level: str
    source: str
    raw: str

    @classmethod
    @orm.declared_attr
    def __tablename__(cls):
        return "log_entries"
