import typing
import uuid

import sqlmodel
from sqlalchemy.ext import asyncio as sqlalchemy_asyncio
from sqlmodel.engine import result
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models import log_entries


class LoggerService:
    async def create_entry(
        self, data: log_entries.LogEntries, database: sqlalchemy_asyncio.AsyncEngine
    ):
        data.id = uuid.uuid4()
        async with AsyncSession(database) as session:
            session.add(data)
            await session.commit()

    async def get_entries(
        self, database: sqlalchemy_asyncio.AsyncEngine
    ) -> result.ScalarResult[typing.Any]:
        async with AsyncSession(database) as session:
            return await session.exec(
                sqlmodel.select(log_entries.LogEntries)  # type: ignore
            )
