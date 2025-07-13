from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey
from datetime import date

from .base import Base


class Author(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    books: Mapped[list["Book"]] = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class Book(Base):

    title: Mapped[str] = mapped_column(nullable=False)
    year_of_manufacture: Mapped[date] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("authors.id", ondelete="CASCADE"),
        nullable=False,
    )
    author: Mapped["Author"] = relationship(
        "Author",
        back_populates="books",
    )
