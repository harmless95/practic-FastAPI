from asyncio import current_task
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
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

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def scoped_session_depends(self):
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(url=settings.db.url, echo=settings.db.echo)
