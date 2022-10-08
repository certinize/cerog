import starlite

from app import events, settings
from app.api import routes


def get_application() -> starlite.Starlite:
    app_settings = settings.app_settings
    start_app = events.get_start_app_handler()
    stop_app = events.get_stop_app_handler()
    cors_config = starlite.CORSConfig(allow_origins=app_settings.allow_origins)

    return starlite.Starlite(
        cors_config=cors_config,
        route_handlers=[routes.route_handlers],
        debug=app_settings.debug,
        on_startup=[start_app],
        on_shutdown=[stop_app],
    )


app = get_application()
