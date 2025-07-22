from typing import TYPE_CHECKING
from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .order import Order
    from .book import Book


class OrderBookAssociation(Base):
    __tablename__ = "order_book_association"
    __table_args__ = (
        UniqueConstraint(
            "book_id",
            "order_id",
            name="idx_unique_order_book",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    count: Mapped[int] = mapped_column(default=1, server_default="1")
    unit_price: Mapped[int] = mapped_column(default=0, server_default="0")

    order: Mapped["Order"] = relationship(
        back_populates="book_details",
    )

    book: Mapped["Book"] = relationship(
        back_populates="order_details",
    )
