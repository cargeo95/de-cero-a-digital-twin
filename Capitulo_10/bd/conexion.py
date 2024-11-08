from pymongo.mongo_client import MongoClient
from pymongo.errors import PyMongoError

# Conexión base de datos
def crearConexion():
    try:
        uri = "mongodb+srv://cagomezj:1234@iot-cluster.sewtzll.mongodb.net/?retryWrites=true&w=majority&appName=iot-cluster"
        client = MongoClient(uri)
        db = client.asentamientos
        return db
    except PyMongoError as e:
        print(f"Error de conexión: {e}")
        return None
