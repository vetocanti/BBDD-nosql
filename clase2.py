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

db = client.sample_guides

#acceder a la colección planets
coll = db.planets

#generar un cursor que busque todos los documentos de la colección planets que en la clave hasRings tenga el valor True

# cursor = coll.find({"hasRings": False, "mainAtmosphere": "Ar"})
# #imprimir los documentos que cumplen la condición

# for doc in cursor:
#     print(doc)
   
   
"""$gt: Greater than
$gte: Greater than or equal to
$lt: Less than
$lte: Less than or equal to
$ne: Not equal to
$eq: Equal to"""   
 
cursor2 = coll.find({"surfaceTemperatureC.max": {"$gt": 200}})

# for doc in cursor2:
#     print(doc)
    
#AND implítico
# cursor3 = coll.find(
#     {"surfaceTemperatureC.mean": {"$lt": 15}, "surfaceTemperatureC.min": {"$gt": -100}}
# )

#AND EXPLÍCITO
# cursor = coll.find(
#     {"$and": [{"orderFromSun": {"$gt": 2}}, {"orderFromSun": {"$lt": 5}}]}
# )

#OR
cursor = coll.find(
    {
        "$or": [
            {"orderFromSun": {"$gt": 7}},
            {"orderFromSun": {"$lt": 2}},
        ]
    }
)


for doc in cursor:
    print(doc)
#cerrar la conexión
client.close()