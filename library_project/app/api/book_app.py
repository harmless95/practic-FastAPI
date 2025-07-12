from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter
from sqlalchemy import select

from library_project.core_app.models import (
    Author as AuthorModel,
    Book as BookModel,
    get_session,
)
from library_project.app.schemas.create_new_book import NewBook


router = APIRouter(prefix="/book", tags=["Book"])


@router.post("/add")
async def add_new_book(data: NewBook, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(AuthorModel).where(
            AuthorModel.name == data.author.name,
            AuthorModel.surname == data.author.surname,
        )
    )
    author = result.scalars().first()
    if not author:
        author = AuthorModel(name=data.author.name, surname=data.author.surname)
        session.add(author)
        await session.flush()
    book = BookModel(
        title=data.title, year_of_manufacture=data.year_of_manufacture, author=author
    )
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return {
        "id": book.id,
        "title": book.title,
        "year_of_manufacture": book.year_of_manufacture,
        "author": {
            "name": author.name,
            "surname": author.surname,
        },
    }
