from typing import List, Annotated
from pydantic import BaseModel, Field
from .book_schema import Book


class Author(BaseModel):
    name: str
    surname: str
    books: Annotated[List[Book], Field(default_factory=list)]

    class Config:
        from_attributes = True
