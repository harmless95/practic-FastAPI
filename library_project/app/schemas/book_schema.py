from pydantic import BaseModel, field_validator, Field, ConfigDict
from datetime import date
from typing import Annotated


class Book(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    year_of_manufacture: Annotated[
        date,
        Field(description="Год выпуска книги"),
    ]

    @field_validator("year_of_manufacture")
    def check_year(cls, v: date) -> date:
        if v.year > 2025:
            raise ValueError("Год не может быть больше 2025 года")
        return v
