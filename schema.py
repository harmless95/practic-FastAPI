from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date


class Author(BaseModel):
    name: str
    surname: str

class Book(BaseModel):
    title: str
    author: Optional[Author] = None
    year_of_manufacture: date = Field(
        ...,
        description="Год выпуска книги"
    )

    @field_validator("year_of_manufacture")
    def check_year(cls, v: date) -> date:
        if v.year > 2025:
            raise ValueError("Год не может быть больше 2025 года")
        return v