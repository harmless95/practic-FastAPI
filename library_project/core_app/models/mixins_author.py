from typing import TYPE_CHECKING

from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .author import Author


class MixinAuthor:
    _author_unique: bool = False
    _author_nullable: bool = False
    _author_ondelete: str = False
    _author_back_populates: str | None = None

    @declared_attr
    def author_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "authors.id",
                ondelete=cls._author_ondelete,
            ),
            unique=cls._author_unique,
            nullable=cls._author_nullable,
        )

    @declared_attr
    def author(cls) -> Mapped["Author"]:
        return relationship(
            "Author",
            back_populates=cls._author_back_populates,
        )
