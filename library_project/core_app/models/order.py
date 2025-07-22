from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func

from .base import Base


if TYPE_CHECKING:
    from .book import Book
    from .order_book_association import OrderBookAssociation


class Order(Base):
    promocode: Mapped[str | None]
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now()
    )
    # books: Mapped[list["Book"]] = relationship(
    #     secondary="order_book_association",
    #     back_populates="orders",
    #     # lazy="noload",
    # )

    book_details: Mapped[list["OrderBookAssociation"]] = relationship(
        back_populates="order",
    )
