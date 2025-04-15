#importar librerias 
from pymongo import MongoClient

# esta uri es propia de su cluster de mongo db
# uri = "mongodb+srv://<db_username>:<db_password>@bbddnosql.4zb9ljj.mongodb.net/?retryWrites=true&w=majority&appName=BBDDNoSql"
"""mongodb+srv://<db_username>:<db_password>@bbddnosql.4zb9ljj.mongodb.net/?retryWrites=true&w=majority&appName=BBDDNoSql
<db_username> = nombre de usuario
<db_password> = contraseña de usuario
Deben configurar su red en network access.
"""


#generar conexión mediante cliente
client = MongoClient(uri)

#acceder a base de datos sample_guides

db = client.sample_guides

#acceder a la colección planets
coll = db.planets

#generar un cursor que busque todos los documentos de la colección planets que en la clave hasRings tenga el valor True

cursor = coll.find({"hasRings": True})

#imprimir los documentos que cumplen la condición

for doc in cursor:
    print(doc)
    
    
#cerrar la conexión
client.close()