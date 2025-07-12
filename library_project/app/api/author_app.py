from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter

from library_project.core_app.models import get_session
from library_project.app.files_crud.author_crud import (
    get_authors,
    get_author,
    create_author,
)
from library_project.app.schemas.create_new_author import NewAuthor

router = APIRouter(prefix="/author", tags=["Author"])


@router.get("/{author_id}/")
async def get_user_by_id(author_id: int, session: AsyncSession = Depends(get_session)):
    return await get_author(session=session, author_id=author_id)


@router.get("/")
async def get_all_authors(session: AsyncSession = Depends(get_session)):
    return await get_authors(session=session)


@router.post("/")
async def new_author(data: NewAuthor, session: AsyncSession = Depends(get_session)):
    return await create_author(session=session, data=data)
