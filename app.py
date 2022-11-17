from fastapi import FastAPI
from Routes.user import user 
from Routes.array import array


app = FastAPI()

app.include_router(user)

app.include_router(array)

