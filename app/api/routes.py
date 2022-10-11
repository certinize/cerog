import starlite

from app.api.controllers import health, logger

route_handlers = starlite.Router(
    path="/",
    route_handlers=[logger.LoggerController, health.HealthController],
)
