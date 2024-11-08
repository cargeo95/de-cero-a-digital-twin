#Realizamos conexión a base de datos
from .conexion import crearConexion
db = crearConexion()

#Read all - Sensores Acelerometro
def readAcelerometroDB():
    consulta = db.sensorAcelerometro.find_one(sort=[('tiempo', -1)])
    return consulta

#Read all - Sensores Distancia 1
def readDistancia1DB():
    consulta = db.sensorDistancia1.find_one(sort=[('tiempo', -1)])
    return consulta

#Read all - Sensores Distancia 2
def readDistancia2DB():
    consulta = db.sensorDistancia2.find_one(sort=[('tiempo', -1)])
    return consulta

#Read all - Sensores Vibración 1
def readVibracion1DB():
    consulta = db.sensorVibracion1.find_one(sort=[('tiempo', -1)])
    return consulta

#Read all - Sensores Vibración 2
def readVibracion2DB():
    consulta = db.sensorVibracion2.find_one(sort=[('tiempo', -1)])
    return consulta

#Read all - Sensores Vibración 3
def readVibracion3DB():
    consulta = db.sensorVibracion3.find_one(sort=[('tiempo', -1)])
    return consulta

