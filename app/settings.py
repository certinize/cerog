import pydantic


class Settings(pydantic.BaseSettings):
    debug: bool = False
    allow_origins: list[str] = ["*"]
    database_url: pydantic.PostgresDsn | None = None
    min_connection_count = 10
    max_connection_count = 10

    @property
    def sqlalchemy_kwargs(self) -> dict[str, bool | int]:
        return {
            "future": True,
            "pool_size": self.min_connection_count,
            "max_overflow": self.max_connection_count,
        }

    class Config(pydantic.BaseSettings.Config):
        env_file = ".env"


app_settings = Settings()
