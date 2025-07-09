import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from  sqlalchemy import (select)

import models
from database import get_session, engine
from models import Author as AuthorModel, Book as BookModel
from schema import NewBook

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.get("/")
def get_hello():
    return {"message": "Hello world"}

@app.get("/name/")
def get_username(user: str = "User"):
    return {"message": f"Hello, {user}"}

@app.get("/base/author/{user_id}/")
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    base_command = select(AuthorModel).where(AuthorModel.id==user_id)
    result = await session.execute(base_command)
    author = result.scalars().first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@app.post("/base/add")
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



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)