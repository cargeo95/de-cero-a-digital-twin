from pymongo.mongo_client import MongoClient
import datetime

uri = "mongodb+srv://cargomezj:1234@cluster0.8hbnrv6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client.Deslizamientos

#create
def createCoordenada(entradaDatoX,entradaDatoY):
    
    data = {
        "nombre" : "sensor_4",
        "coordenada_X": entradaDatoX,
        "coordenada_Y":  entradaDatoY,
        "rol": "distancia",
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
        
    }
    
    result = db.sensores.insert_one(data)
    
    if result.acknowledged:
        return "se realizó con éxito"
    else:
        return "no se ejecutó"
   
#READ!!!!!

def readSensor():
    # Consultar la colección Sensor_1
    consulta = list(db.Sensor_1.find())
    
    #crear lista y su respectivo diccionario 
    resultado_tabla = []
    for i in consulta:
        fila = {
            "Distancia" : i["distance"],
            "Create" : i["created_at"],
            "Update" :i["updated_at"]
        }
        resultado_tabla.append(fila)
    
    return resultado_tabla



#READ_ONE

def readSensorUnico(valorBuscado):
    result = db.sensores.find_one({"nombre": valorBuscado})
    if result:
        coordenada_X = result.get("coordenada_X")
        coordenada_Y = result.get("coordenada_Y")
        return coordenada_X,coordenada_Y
    
    else:
        return "No se encontró resultado"
