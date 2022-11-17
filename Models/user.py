from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    name: str
    last_name: str
    identification: int
    numero: Union[int, None] = None
    password: str

