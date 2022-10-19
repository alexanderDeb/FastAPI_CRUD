import pymongo
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI

conection = MongoClient(
    "mongodb+srv://Alexander:1234@cluster.wc0ampm.mongodb.net/?retryWrites=true&w=majority")
db = conection.test
mydb = conection["EstructuraDatosPrueba"]  # nombre de la base de datos
mycol = mydb["Usuario"]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


# Endpoint para listar los usuarios de la base de datos
@app.get("/user")
async def GetUser():
    info = []
    for y in mycol.find():
        print(y)
        info.append((y["name"], y["last_name"],
                    y["identification"], y["numero"]))
    return {
        "Usuario": info
    }

# Endpoint para filtrar por identificador via params


@app.get("/user/identification/{id}")
async def Item(id: int):
    y = mycol.find_one({"identification": id})
    print(y)
    return {
        "nombre": y["name"],
        "Apellido": y["last_name"],
        "numero": y["numero"]
    }

class Item(BaseModel):
    name: str
    last_name: str
    identification: int
    numero: Union[int, None] = None


@app.put("/user/edit/identification/{id}")
async def update_item(id: int , user: Item):
    mycol.find_one_and_update({"identification": id}, {"$set":dict(user)})
    return("se creo correctamente")


@app.post("/user/create")
async def create_item(item: Item):
    data = {
        "name": item.name,
        "last_name": item.last_name,
        "identification": item.identification,
        "numero": item.numero,
    }
    mycol.insert_one(data)
    return (f"se edito exitosamente el usuario")


@app.delete("/user/delete/identification/{id}")
async def Item(id: int):
    y = mycol.find_one_and_delete({"identification": id})
    print(y)
    if (y != None):
        return {
            "message": "se ha eliminado con exito"
        }
    else:
        return{
            "message": "el usuario no existe"
        }
