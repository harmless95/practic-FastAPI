from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter

from library_project.app.models_file.models import Author as AuthorModel, Book as BookModel
from library_project.app.schemas.create_new_book import NewBook
from library_project.database.config import get_session

router = APIRouter(prefix="/book", tags=["Book"])

@router.post("/add")
async def add_new_book(data: NewBook, session: AsyncSession = Depends(get_session)):
    author = AuthorModel(
        name=data.author.name,
        surname=data.author.surname
    )
    book = BookModel(
        title=data.title,
        year_of_manufacture=data.year_of_manufacture,
        author=author
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
        }
    }