import pydantic
import sqlmodel
import starlite
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine

from app.settings import app_settings


async def create_db_engine(state: starlite.State) -> None:
    assert isinstance(app_settings.database_url, pydantic.PostgresDsn)
    database_url = app_settings.database_url.replace(
        "postgres://", "postgresql+asyncpg://"
    )
    state.engine = create_async_engine(database_url, **app_settings.sqlalchemy_kwargs)


async def dispose_db_engine(state: starlite.State) -> None:
    await state.engine.dispose()


async def create_db_tables(state: starlite.State) -> None:
    engine_ = state.engine

    if isinstance(engine_, AsyncEngine):
        async with engine_.begin() as conn:
            await conn.run_sync(sqlmodel.SQLModel.metadata.create_all)
    else:
        raise ValueError(
            "sqlalchemy.ext.asyncio.engine.AsyncEngine is missing from starlite.State"
        )


def get_start_app_handler():
    async def start_app(state: starlite.State) -> None:
        await create_db_engine(state)
        await create_db_tables(state)

    return start_app


def get_stop_app_handler():
    async def stop_app(state: starlite.State) -> None:
        await dispose_db_engine(state)

    return stop_app
