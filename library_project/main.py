import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from library_project.core_app.models import Base, db_helper
from library_project.app.api import author_router, book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(author_router)
app.include_router(book_router)


@app.get("/")
def get_hello():
    return {"message": "Hello world"}


@app.get("/name/")
def get_username(user: str = "User"):
    return {"message": f"Hello, {user}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
