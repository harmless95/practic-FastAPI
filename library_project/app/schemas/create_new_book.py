from pydantic import BaseModel, ConfigDict
from .book_schema import Book
from .create_new_author import NewAuthor


class NewBook(Book):
    model_config = ConfigDict(from_attributes=True)
    author: NewAuthor
