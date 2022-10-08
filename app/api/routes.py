import starlite

from app.api.controllers import logger

route_handlers = starlite.Router(
    path="/",
    route_handlers=[
        logger.LoggerController,
    ],
)
