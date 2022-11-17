from fastapi import APIRouter
from Config.db import conection
from Schemas.array import arraysEntity, arrayEntity
from Models.array import Array
from bson import ObjectId

array = APIRouter()

@array.get('/arrays')
def find_all_arrays():
    return arraysEntity(conection.EstructuraDatosPrueba.Arreglos.find())


@array.get('/array/{id}')
def get_array(id: str):
    return arrayEntity(conection.EstructuraDatosPrueba.Arreglos.find_one({"_id": ObjectId(id)}))


@array.post('/array')
def create_array(array: Array):
    new_array = dict(array)
    id = conection.EstructuraDatosPrueba.Arreglos.insert_one(new_array).inserted_id
    array = conection.EstructuraDatosPrueba.Arreglos.find_one({"_id": id})
    return arrayEntity(array)

@array.delete('/array/{id}')
def delete_array(id: str):
    data = arrayEntity(conection.EstructuraDatosPrueba.Arreglos.find_one({"_id": ObjectId(id)}))
    data["data"].pop()
    conection.EstructuraDatosPrueba.Arreglos.find_one_and_update({"_id": ObjectId(id)},{"$set":data})
    return data

