import pydantic


class LogEntry(pydantic.BaseModel):
    id: pydantic.UUID4
    message: str
