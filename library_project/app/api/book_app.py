from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter, HTTPException, status

from library_project.app.schemas.book_schema import Book, BookUpdate, BookUpdatePartial
from library_project.core_app.models import db_helper
from library_project.app.files_crud.dependencies import depend_book_by_id

from library_project.app.schemas.create_new_book import NewBook
from library_project.app.files_crud.book_crud import (
    get_books,
    book_by_id,
    new_book,
    update_book,
    delete_book,
)


router = APIRouter(prefix="/book", tags=["Book"])


@router.get("/", response_model=list[Book])
async def get_all_books(
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
):
    return await get_books(session=session)


@router.get("/{book_id}/")
async def get_book_by_id(
    book: Book = Depends(
        depend_book_by_id,
    )
):
    return book


@router.post(
    "/add",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
async def add_new_book(
    data: NewBook,
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
):
    return await new_book(session=session, data=data)


@router.put("/{book_id/}")
async def update_book(
    book_update: BookUpdate,
    book: Book = Depends(depend_book_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
) -> Book:
    return await update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


@router.patch("/{book_id/}")
async def update_book(
    book_update: BookUpdatePartial,
    book: Book = Depends(depend_book_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
) -> Book:
    return await update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True,
    )


@router.delete("/{book_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
    book: Book = Depends(depend_book_by_id),
):
    await delete_book(session=session, book=book)
