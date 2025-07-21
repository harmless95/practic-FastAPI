from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

from .base import Base
from .mixins_author import MixinAuthor
from .order_book_association import order_book_association_table

if TYPE_CHECKING:
    from .order import Order


class Book(MixinAuthor, Base):
    _author_back_populates = "books"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    year_of_manufacture: Mapped[date] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    orders: Mapped[list["Order"]] = relationship(
        secondary=order_book_association_table, back_populates="books"
    )
