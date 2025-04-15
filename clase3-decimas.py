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
    {"name": "Python", "duration": 3, "students": 20},
    {"name": "Java", "duration": 4, "students": 15},
    {"name": "JavaScript", "duration": 2, "students": 25},
]

result = coll.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents.")



client.close()