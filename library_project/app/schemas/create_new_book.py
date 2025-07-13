from pydantic import BaseModel, ConfigDict
from .book_schema import Book
from .author_schema import NewAuthor


class NewBook(Book):
    model_config = ConfigDict(from_attributes=True)
    author: NewAuthor
