#importar librerias 
from pymongo import MongoClient

# esta uri es propia de su cluster de mongo db
uri = "mongodb+srv://<db_username>:<db_password>@bbddnosql.4zb9ljj.mongodb.net/?retryWrites=true&w=majority&appName=BBDDNoSql"
"""mongodb+srv://<db_username>:<db_password>@bbddnosql.4zb9ljj.mongodb.net/?retryWrites=true&w=majority&appName=BBDDNoSql
<db_username> = nombre de usuario
<db_password> = contraseña de usuario
Deben configurar su red en network access.
"""


#generar conexión mediante cliente
client = MongoClient(uri)

#acceder a base de datos sample_guides

db = client.estudiantes

#acceder a la colección planets
coll = db.cursos

docs = [
    {"name": "Python", "duration": 3, "students": 100},
    {"name": "Java", "duration": 4, "students": 0},
    {"name": "JavaScript", "duration": 2, "students": 60},
]

result = coll.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents.")

#modificar documentos
# $set: update the value of a field in a document
# $inc: increment the value of a field in a document
# $push: add an item to an array in a document
# $pull: remove an item from an array in a document
# $addToSet: add an item to an array in a document only if it does not already exist
# $rename: rename a field in a document
# $unset: remove a field from a document
# $currentDate: set the value of a field to the current date
# $bit: perform bitwise operations on a field in a document
# $mul: multiply the value of a field in a document by a specified value
# $min: update the value of a field in a document only if the specified value is less than the current value
# $max: update the value of a field in a document only if the specified value is greater than the current value
# $rename: rename a field in a document

#Update
myquery = {"name": {"$regex":"^J"}}

doc = {
    "$set":{"duration":40}
}

result = coll.update_many(myquery,doc)
# display the results of your operation
print("Number of documents updated: ", result.modified_count)

#Delete

doc = {
    "students": {
        "$gt":10,
        "$lt":100
    }
}

result = coll.delete_many(doc)
# amount deleted code goes here
print("Number of documents deleted: ", result.deleted_count)

#eliminar base de datos
# client.drop_database("estudiantes")

#eliminar colleciones
new_coll = client.estudiantes.personas


docs = [
        {"name": "Python", "duration": 3, "students": 100},
    {"name": "Java", "duration": 4, "students": 0},
    {"name": "JavaScript", "duration": 2, "students": 60},
]

result = new_coll.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents.")
client.estudiantes.drop_collection("cursos")

client.close()