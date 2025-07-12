from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter
from sqlalchemy import select

from library_project.core_app.models import (
    Author as AuthorModel,
    Book as BookModel,
    get_session,
)
from library_project.app.schemas.create_new_book import NewBook
from library_project.app.files_crud.book_crud import get_books, book_by_id, new_book


router = APIRouter(prefix="/book", tags=["Book"])


@router.get("/")
async def get_all_books(session):
    return await get_books(session=session)


@router.get("/{book_id}/")
async def get_book_by_id(session, book_id: int):
    return await book_by_id(session=session, book_id=book_id)


@router.post("/add")
async def add_new_book(data: NewBook, session: AsyncSession = Depends(get_session)):
    return await new_book(session=session, data=data)

    # result = await session.execute(
    #     select(AuthorModel).where(
    #         AuthorModel.name == data.author.name,
    #         AuthorModel.surname == data.author.surname,
    #     )
    # )
    # author = result.scalars().first()
    # if not author:
    #     author = AuthorModel(name=data.author.name, surname=data.author.surname)
    #     session.add(author)
    #     await session.flush()
    # book = BookModel(
    #     title=data.title, year_of_manufacture=data.year_of_manufacture, author=author
    # )
    # session.add(book)
    # await session.commit()
    # await session.refresh(book)
    # return {
    #     "id": book.id,
    #     "title": book.title,
    #     "year_of_manufacture": book.year_of_manufacture,
    #     "author": {
    #         "name": author.name,
    #         "surname": author.surname,
    #     },
    # }
