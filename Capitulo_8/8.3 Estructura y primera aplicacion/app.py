import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math

#importamos frontend
from fronted.frontend import layout
#importamos backend
from backend.backend import backendPoderoso

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout


#Parte lógica
@app.callback(
    Output('salidaCirculo', 'children'),
    Input('entradaCirculo', 'value'),
)

def areaCirculo(entradaCirculo):
    areaCalculadaCirculo = math.pi * (entradaCirculo**2)
    return 'El área del circulo es: ' + str(areaCalculadaCirculo)

#Calculamos área de un triangulo
@app.callback(
    Output('salidaTriangulo', 'children'),
    Input('entradaBaseTriangulo', 'value'),
    Input('entradaAlturaTriangulo', 'value')
)

def areaTriangulo(entradaBaseTriangulo, entradaAlturaTriangulo):
    areaTriangulo = 0.5 * entradaBaseTriangulo * entradaAlturaTriangulo
    return 'El área del triangulo es: ' + str(areaTriangulo)

#operaciones matemáticas muy extensas y complejas para un backend
@app.callback(
    Output('salidaValor','children'),
    Input('entradaValor','value')
)

def operacionExtensa(entradaValor):
    resultadoC = backendPoderoso(entradaValor)
    return 'el resultado es:' +str(resultadoC)
   

if __name__ == '__main__':
    app.run_server(debug=True)