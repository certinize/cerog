import starlite


class HealthController(starlite.Controller):
    path = "/healthz"

    @starlite.get()
    async def get_entries(self) -> dict[str, str | int]:
        return {"deatil": "I'm alive!", "status_code": 200}
