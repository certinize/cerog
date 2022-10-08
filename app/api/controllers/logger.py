import typing

import starlite
from sqlalchemy.ext import asyncio as sqlalchemy_asyncio

from app.api.dependencies import database
from app.api.services import logger
from app.models import log_entries


class LoggerController(starlite.Controller):
    path = "/logs"

    dependencies: dict[str, "starlite.Provide"] | None = {
        "database": starlite.Provide(database.get_db_engine),
        "logger_service": starlite.Provide(logger.LoggerService),
    }

    @starlite.post()
    async def create_entry(
        self,
        data: log_entries.LogEntries,
        database: sqlalchemy_asyncio.AsyncEngine,
        logger_service: logger.LoggerService,
    ) -> log_entries.LogEntries:
        await logger_service.create_entry(data, database)
        return data

    @starlite.get()
    async def get_entries(
        self,
        database: sqlalchemy_asyncio.AsyncEngine,
        logger_service: logger.LoggerService,
    ) -> dict[str, list[typing.Any]]:
        result = await logger_service.get_entries(database)
        return {"logs": result.all()}
