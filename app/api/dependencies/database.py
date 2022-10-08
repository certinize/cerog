import starlite
from sqlalchemy.ext.asyncio import engine


def get_db_engine(state: starlite.State):
    if isinstance(state.engine, engine.AsyncEngine):
        return state.engine

    raise ValueError(
        "sqlalchemy.ext.asyncio.engine.AsyncEngine is missing from starlite.State"
    )
