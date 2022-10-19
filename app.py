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


# Endpoint para traer todos los usuarios
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


@app.get("/user/identification/")
async def Item(identification: int):
    y = mycol.find_one({"identification": identification})
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


@app.put("/user/create")
async def create_item(item: Item):

    data = {
        "name": item.name,
        "last_name": item.last_name,
        "identification": item.identification,
        "numero": item.numero,
        "message": "se creo exitosamente el usuario"
    }

    mycol.insert_one(data)
    return(item)


@app.delete("/user/delete/identification/")
async def Item(identification: int):
    y = mycol.find_one_and_delete({"identification": identification})
    print(y)
    if (y != None):
        return {
            "message": "se ha eliminado con exito"
        }
    else:
        return{
            "message": "el usuario no existe"
        }
