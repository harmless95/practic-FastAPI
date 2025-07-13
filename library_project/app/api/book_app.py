from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter, HTTPException, status

from library_project.core_app.models import db_helper

from library_project.app.schemas.create_new_book import NewBook
from library_project.app.files_crud.book_crud import get_books, book_by_id, new_book


router = APIRouter(prefix="/book", tags=["Book"])


@router.get("/")
async def get_all_books(
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
):
    return await get_books(session=session)


@router.get("/{book_id}/")
async def get_book_by_id(
    book_id: int, session: AsyncSession = Depends(db_helper.scoped_session_depends)
):
    book = await book_by_id(session=session, book_id=book_id)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book {book_id} not found!",
    )


@router.post("/add")
async def add_new_book(
    data: NewBook, session: AsyncSession = Depends(db_helper.scoped_session_depends)
):
    return await new_book(session=session, data=data)
