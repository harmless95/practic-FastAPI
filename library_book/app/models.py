from library_book.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship



class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), nullable=False)
    books = relationship("Book",
                         back_populates="author",
                         cascade="all, delete-orphan",
                         passive_deletes=True)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    year_of_manufacture = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))
    author = relationship("Author", back_populates="books")


