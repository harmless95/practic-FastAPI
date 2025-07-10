from .book_schema import Book
from .create_new_author import NewAuthor

class NewBook(Book):
    author: NewAuthor

    class Config:
        orm_mode = True