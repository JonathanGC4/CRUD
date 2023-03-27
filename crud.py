import json
from conection_parameters import collection


def read_biblioteca(id=None):
    if id is not None:
        query = {"_id": id}
        document = collection.find_one(query)
        print(json.dumps(document))

    else:
        documents = collection.find()
        for document in documents:
            print(document)


def create_biblioteca(bibliotecas):
    result = collection.insert_one(bibliotecas)
    print(result.inserted_id)


def update_biblioteca(id, json_indices_values):
    query = {"_id": id}
    new_values = {"$set": json_indices_values}
    result = collection.update_one(query, new_values)
    print(result.modified_count)
