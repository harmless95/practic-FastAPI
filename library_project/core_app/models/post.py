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

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, user_title={self.title!r}, user_id={self.user_id})"

    def __repr__(self):
        return str(self)
