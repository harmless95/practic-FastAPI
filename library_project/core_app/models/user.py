from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base import Base

if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile


class User(Base):
    user_name: Mapped[str] = mapped_column(String(32), unique=True)
    user_surname: Mapped[str] = mapped_column(String(50))

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, user_name={self.user_name}, user_surname={self.user_surname})"

    def __repr__(self):
        return str(self)
