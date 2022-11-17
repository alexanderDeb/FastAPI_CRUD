def userEntity(item) -> dict:
    return{
        "id": str(item['_id']),
        'name': item['name'],
        'last_name': item['last_name'],
        'identification': item['identification'],
        'numero': item['numero'],
        'password': item['password']
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

