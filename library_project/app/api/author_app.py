from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Path, APIRouter
from sqlalchemy import select

from library_project.core_app.models import db_helper
from library_project.core_app.models import Author as AuthorModel

router = APIRouter(prefix="/author", tags=["Author"])
get_session = db_helper.session_factory


@router.get("/{user_id}/")
async def get_user_by_id(
    user_id: Annotated[int, Path(ge=1, lt=1_000_000)],
    session: AsyncSession = Depends(get_session),
):
    base_command = select(AuthorModel).where(AuthorModel.id == user_id)
    result = await session.execute(base_command)
    author = result.scalars().first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.get("/")
async def get_all_authors(session: AsyncSession = Depends(get_session)):
    base_command = select(AuthorModel)
    result = await session.execute(base_command)
    authors = result.scalars().all()
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found")
    return authors
