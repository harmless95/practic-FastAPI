from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

from .base import Base
from .mixins import UserRelationMixin


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"
    title: Mapped[str] = mapped_column(String(100), unique=True)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
