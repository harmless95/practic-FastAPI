from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins_author import MixinAuthor


class Book(MixinAuthor, Base):
    _author_back_populates = "books"

    title: Mapped[str] = mapped_column(nullable=False)
    year_of_manufacture: Mapped[date] = mapped_column(nullable=False)
