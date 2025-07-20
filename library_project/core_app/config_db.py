from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{(BASE_DIR / 'library.db').as_posix()}"
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()


settings = Settings()
