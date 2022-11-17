from pydantic import BaseModel

class Array(BaseModel):
  name: str
  data: list