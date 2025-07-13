from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter, HTTPException, status

from library_project.core_app.models import db_helper
from library_project.app.files_crud.author_crud import (
    get_authors,
    get_author,
    create_author,
    update_author,
    delete_author,
)
from library_project.app.files_crud.dependencies import author_by_id
from library_project.app.schemas.author_schema import (
    Author,
    AuthorUpdate,
    NewAuthor,
    AuthorUpdatePartial,
)

router = APIRouter(prefix="/author", tags=["Author"])


@router.get("/{author_id}/", response_model=Author)
async def get_user_by_id(
    author: Author = Depends(author_by_id),
):
    return author


@router.get("/", response_model=list[Author])
async def get_all_authors(
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
):
    return await get_authors(session=session)


@router.post(
    "/",
    response_model=Author,
    status_code=status.HTTP_201_CREATED,
)
async def new_author(
    data: NewAuthor,
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
):
    return await create_author(session=session, data=data)


@router.put("/{author_id}/")
async def update_author_by_id(
    author_update: AuthorUpdate,
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(
        db_helper.scoped_session_depends,
    ),
):
    return await update_author(
        session=session,
        author=author,
        author_update=author_update,
    )


@router.patch("/{author_id}/")
async def update_author_by_id(
    author_update: AuthorUpdatePartial,
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(
        db_helper.scoped_session_depends,
    ),
):
    return await update_author(
        session=session,
        author=author,
        author_update=author_update,
        partial=True,
    )


@router.delete("/{author_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author_by_id(
    session: AsyncSession = Depends(db_helper.scoped_session_depends),
    author: Author = Depends(author_by_id),
) -> None:
    await delete_author(session=session, author=author)
