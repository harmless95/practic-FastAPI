from typing import List, Annotated
from pydantic import BaseModel, Field, ConfigDict
from .book_schema import Book


class Author(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str
    books: Annotated[List[Book], Field(default_factory=list)]
