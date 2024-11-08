#Realizamos conexión a base de datos
from .conexion import crearConexion
db = crearConexion()


#create
def createSensores(nombre,coordenada_X , coordenada_Y,coordenada_Z):
    
    data = {
        "nombre": nombre,
        "coordenada_X" : coordenada_X,
        "coordenada_Y" : coordenada_Y,
        "coordenada_Z" : coordenada_Z
    }
    
    result = db.sensores.insert_one(data)
    if result.acknowledged:
        print("se insertó con éxito")
    else:
        print("algo pasó")
    
# createSensores("sensor_2",7,2,1)


#read
def readSensor():
    consulta = list(db.sensores.find())
    #crear lista y su respectivo diccionario 
    resultado_tabla = []
    for i in consulta:
        fila = {
            "nombre" : i["nombre"],
            "coordenada_X" : i["coordenada_X"],
            "coordenada_Y" :i["coordenada_Y"],
            "coordenada_Z" :i["coordenada_Z"],
        }
        resultado_tabla.append(fila)
    
    return resultado_tabla
