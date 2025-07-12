from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio.session import AsyncSession

from library_project.core_app.config_db import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(url=settings.db_url, echo=settings.db_echo)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with db_helper.session_factory() as session:
        yield session
