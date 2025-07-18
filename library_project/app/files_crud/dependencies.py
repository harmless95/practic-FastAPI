from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from library_project.app.files_crud.author_crud import get_author
from library_project.app.files_crud.book_crud import book_by_id
from library_project.core_app.models import db_helper, Author, Book


async def author_by_id(
    author_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
) -> Author:
    author = await get_author(session=session, author_id=author_id)
    if author is not None:
        return author
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"author {author_id} not found!",
    )


async def depend_book_by_id(
    book_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
) -> Book:
    book = await book_by_id(session=session, book_id=book_id)
    if book is not None:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"author {book_id} not found!",
    )
