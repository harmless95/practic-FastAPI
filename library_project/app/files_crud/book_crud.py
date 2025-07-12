from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from library_project.core_app.models import Book as BookModel, Author as AuthorModel
from library_project.app.schemas.create_new_book import NewBook


async def get_books(session: AsyncSession) -> list[BookModel]:
    stmt = select(BookModel).order_by(BookModel.id)
    result: Result = await session.execute(stmt)
    books = result.scalars().all()
    return list(books)


async def book_by_id(session: AsyncSession, book_id: int) -> BookModel | None:
    return await session.get(BookModel, book_id)


async def new_book(session: AsyncSession, data: NewBook) -> NewBook:
    result = await session.execute(
        select(AuthorModel).where(
            AuthorModel.name == data.author.name,
            AuthorModel.surname == data.author.surname,
        )
    )
    author = result.scalars().first()
    if not author:
        author = AuthorModel(
            name=data.author.name,
            surname=data.author.surname,
        )
        session.add(author)
        await session.flush()
    book = BookModel(
        title=data.title,
        year_of_manufacture=data.year_of_manufacture,
        author=author,
    )
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return NewBook(
        title=book.title,
        year_of_manufacture=book.year_of_manufacture,
        author=data.author,
    )
