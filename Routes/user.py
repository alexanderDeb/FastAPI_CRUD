from fastapi import APIRouter, Response
from Config.db import conection
from Schemas.user import userEntity, usersEntity
from Models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get('/users')
def find_all_user():
    return usersEntity(conection.EstructuraDatosPrueba.Usuario.find())


@user.get('/user/{id}')
def Get_User(id: str):
    return userEntity(conection.EstructuraDatosPrueba.Usuario.find_one({"_id": ObjectId(id)}))


@user.post('/user')
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = conection.EstructuraDatosPrueba.Usuario.insert_one(new_user).inserted_id
    user = conection.EstructuraDatosPrueba.Usuario.find_one({"_id": id})
    return userEntity(user)


@user.put('/user/{id}')
def update_user(id: str, user: User):
    edit_user = dict(user)
    edit_user["password"] = sha256_crypt.encrypt(edit_user["password"])
    conection.EstructuraDatosPrueba.Usuario.find_one_and_update({"_id": ObjectId(id)},{"$set":edit_user})
    return userEntity(conection.EstructuraDatosPrueba.Usuario.find_one({"_id":ObjectId(id)}))


@user.delete('/user/{id}')
def delete_user(id: str):
    userEntity(conection.EstructuraDatosPrueba.Usuario.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

