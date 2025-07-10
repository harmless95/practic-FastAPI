from typing import Optional, List
from pydantic import BaseModel
from .book_schema import Book

class Author(BaseModel):
    name: str
    surname: str
    books: Optional[List[Book]] = None

    class Config:
        orm_mode = True
