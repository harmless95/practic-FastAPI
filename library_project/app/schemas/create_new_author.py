from pydantic import BaseModel

class NewAuthor(BaseModel):
    name: str
    surname: str