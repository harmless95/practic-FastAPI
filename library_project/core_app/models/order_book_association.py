from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from .base import Base

order_book_association_table = Table(
    "order_book_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", ForeignKey("books.id"), nullable=False),
    Column("order_id", ForeignKey("orders.id"), nullable=False),
    UniqueConstraint("book_id", "order_id", name="idx_unique_order_book"),
)
