from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter, HTTPException, status

from library_project.core_app.models import get_session
from library_project.app.files_crud.author_crud import (
    get_authors,
    get_author,
    create_author,
)
from library_project.app.schemas.create_new_author import NewAuthor
from library_project.app.schemas.author_schema import Author

router = APIRouter(prefix="/author", tags=["Author"])


@router.get("/{author_id}/", response_model=Author)
async def get_user_by_id(author_id: int, session: AsyncSession = Depends(get_session)):
    author = await get_author(session=session, author_id=author_id)
    if author is not None:
        return author
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"author {author_id} not found!",
    )


@router.get("/", response_model=list[Author])
async def get_all_authors(session: AsyncSession = Depends(get_session)):
    return await get_authors(session=session)


@router.post("/", response_model=Author)
async def new_author(data: NewAuthor, session: AsyncSession = Depends(get_session)):
    return await create_author(session=session, data=data)
