from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import date


class Book(BaseModel):
    title: str
    year_of_manufacture: date = Field(
        ...,
        description="Год выпуска книги"
    )

    @field_validator("year_of_manufacture")
    def check_year(cls, v: date) -> date:
        if v.year > 2025:
            raise ValueError("Год не может быть больше 2025 года")
        return v

class Author(BaseModel):
    name: str
    surname: str
    books: Optional[List[Book]] = None