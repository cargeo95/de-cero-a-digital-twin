from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
from frontend.layout import layout
import plotly.graph_objs as go

#conexión base de datos
from bd.senoresController import readAcelerometroDB
from bd.senoresController import readDistancia1DB
from bd.senoresController import readDistancia2DB
from bd.senoresController import readVibracion1DB
from bd.senoresController import readVibracion2DB
from bd.senoresController import readVibracion3DB

data_readAcelerometroDB_X = []
data_readAcelerometroDB_Y = []
data_readDistancia1DB = []
data_readDistancia2DB = []
data_readVibracion1DB = []
data_readVibracion2DB = []
data_readVibracion3DB = []

tiempo_readAcelerometroDB_X = []
tiempo_readAcelerometroDB_Y = []
tiempo_readDistancia1DB = []
tiempo_readDistancia2DB = []
tiempo_readVibracion1DB = []
tiempo_readVibracion2DB = []
tiempo_readVibracion3DB = []

#conexión background
from background.sensor4xBG import create_figure_S4X
from background.sensor4yBG import create_figure_S4Y
from background.sensorDistancia1BG import create_figure_D1
from background.sensorDistancia2BG import create_figure_D2
from background.sensorV1BG import create_figure_V1
from background.sensorV2BG import create_figure_V2
from background.sensorV3BG import create_figure_V3


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = layout


#  ACTUALIZAR GRÁFICA SENSOR 4X
@app.callback(
    Output('sensorAceX', 'figure'),
    Input('interval-sensorAceX', 'n_intervals'),
)
def actualizacionFigura(n):
    data = readAcelerometroDB()
    data_readAcelerometroDB_X.append(float(data['aceleracion_X']))
    tiempo_readAcelerometroDB_X.append(data['tiempo'])
    
    # Mantener solo los últimos 20 valores
    if len(data_readAcelerometroDB_X) > 10:
        data_readAcelerometroDB_X.pop(0)
        tiempo_readAcelerometroDB_X.pop(0)
        
    figure = create_figure_S4X(tiempo_readAcelerometroDB_X, data_readAcelerometroDB_X)
    return figure

#  ACTUALIZAR GRÁFICA SENSOR 4Y
@app.callback(
    Output('sensorAceY', 'figure'),
    Input('interval-sensorAceY', 'n_intervals'),
)
def actualizacionFigura(n):
    data = readAcelerometroDB()
    data_readAcelerometroDB_Y.append(float(data['aceleracion_Y']))
    tiempo_readAcelerometroDB_Y.append(data['tiempo'])
    
    # Mantener solo los últimos 20 valores
    if len(data_readAcelerometroDB_Y) > 10:
        data_readAcelerometroDB_Y.pop(0)
        tiempo_readAcelerometroDB_Y.pop(0)
    
    figure = create_figure_S4Y(tiempo_readAcelerometroDB_Y, data_readAcelerometroDB_Y)
    return figure

#  ACTUALIZAR GRÁFICA DISTANCIA 1
@app.callback(
    Output('sensorDistancia1', 'figure'),
    Input('interval-sensorDistancia1', 'n_intervals'),
)
def actualizacionFigura(n):
    data = readDistancia1DB()
    data_readDistancia1DB.append(float(data['distancia']))
    tiempo_readDistancia1DB.append(data['tiempo'])
    
    # Mantener solo los últimos 20 valores
    if len(data_readDistancia1DB) > 10:
        data_readDistancia1DB.pop(0)
        tiempo_readDistancia1DB.pop(0)
        
    figure = create_figure_D1(tiempo_readDistancia1DB, data_readDistancia1DB)    
    return figure
                
#  ACTUALIZAR GRÁFICA DISTANCIA 2
@app.callback(
    Output('sensorDistancia2', 'figure'),
    Input('interval-sensorDistancia2', 'n_intervals'),
)
def actualizacionFigura(n):
    data = readDistancia2DB()
    data_readDistancia2DB.append(float(data['distancia']))
    tiempo_readDistancia2DB.append(data['tiempo'])

    # Mantener solo los últimos 20 valores
    if len(data_readDistancia2DB) > 10:
        data_readDistancia2DB.pop(0)
        tiempo_readDistancia2DB.pop(0)    
    
    figure = create_figure_D2(tiempo_readDistancia2DB, data_readDistancia2DB)   
    return figure

#  ACTUALIZAR GRÁFICA VIBRACION 1
@app.callback(
    Output('sensorVibracion1', 'figure'),
    Input('interval-sensorVibracion1', 'n_intervals'),
)
def actualizacionFigura(n):
    data = readVibracion1DB()
    data_readVibracion1DB.append(data['estado'])
    tiempo_readVibracion1DB.append(data['tiempo'])
 
     # Mantener solo los últimos 20 valores
    if len(data_readVibracion1DB) > 10:
        data_readVibracion1DB.pop(0)
        tiempo_readVibracion1DB.pop(0)      
    
    figure = create_figure_V1(tiempo_readVibracion1DB, data_readVibracion1DB)
    return figure

#  ACTUALIZAR GRÁFICA VIBRACION V2
@app.callback(
    Output('sensorVibracion2', 'figure'),
    Input('interval-sensorVibracion2', 'n_intervals'),
)
def actualizacionFigura(n):
    data = readVibracion2DB()
    data_readVibracion2DB.append(data['estado'])
    tiempo_readVibracion2DB.append(data['tiempo'])
 
    # Mantener solo los últimos 20 valores
    if len(data_readVibracion2DB) > 10:
        data_readVibracion2DB.pop(0)
        tiempo_readVibracion2DB.pop(0)        
    
    figure = create_figure_V2(tiempo_readVibracion2DB, data_readVibracion2DB)
    return figure

#  ACTUALIZAR GRÁFICA VIBRACION V3
@app.callback(
    Output('sensorVibracion3', 'figure'),
    Input('interval-sensorVibracion3', 'n_intervals'),
)
def actualizacionFigura(n):
    data = readVibracion3DB()
    data_readVibracion3DB.append(data['estado'])
    tiempo_readVibracion3DB.append(data['tiempo'])
 
     # Mantener solo los últimos 20 valores
    if len(data_readVibracion3DB) > 10:
        data_readVibracion3DB.pop(0)
        tiempo_readVibracion3DB.pop(0)        
    
    figure = create_figure_V3(tiempo_readVibracion3DB, data_readVibracion3DB)    
    return figure


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)
