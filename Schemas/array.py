def arrayEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "data": list(item["data"])
    }


def arraysEntity(entity) -> list:
    return [arrayEntity(item) for item in entity]
