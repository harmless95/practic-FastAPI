import uvicorn
from fastapi import FastAPI

from library_project.app.models_file import models
from library_project.database.config import engine
from library_project.app.api.author_app import router as author_router
from library_project.app.api.book_app import router as book_router

app = FastAPI()
app.include_router(author_router)
app.include_router(book_router)


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


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
