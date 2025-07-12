from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from library_project.core_app.models import Author as AuthorModel
from library_project.app.schemas.create_new_author import NewAuthor
from library_project.app.schemas.author_schema import Author


async def get_authors(session: AsyncSession) -> list[AuthorModel]:
    stmt = select(AuthorModel).order_by(AuthorModel.id)
    result: Result = await session.execute(stmt)
    authors = result.scalars().all()
    return list(authors)


async def get_author(session: AsyncSession, author_id: int) -> AuthorModel | None:
    return await session.get(AuthorModel, author_id)


async def create_author(session: AsyncSession, data: NewAuthor) -> Author:
    result = await session.execute(
        select(AuthorModel)
        .options(selectinload(AuthorModel.books))
        .where(
            AuthorModel.name == data.name,
            AuthorModel.surname == data.surname,
        )
    )
    author = result.scalars().first()
    if not author:
        author = AuthorModel(
            name=data.name,
            surname=data.surname,
        )
        session.add(author)
        await session.flush()
        await session.commit()
        await session.refresh(author, attribute_names=["books"])
    return Author.model_validate(author)
