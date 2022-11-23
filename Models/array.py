from pydantic import BaseModel

class Array(BaseModel):
  name: str
  data: list

class ArrayEdit(BaseModel):
  data: str