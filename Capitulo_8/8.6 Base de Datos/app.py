from dash import Dash, html, Input, Output,dcc,State,dash_table
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

#importamos backend
from bd.conexion import createCoordenada,readSensor , readSensorUnico

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Conexion BD"),
    
    #CREAR
    html.Div([
        html.H1("CREATE"),
        html.H4("Coordenada X:"),
        dcc.Input(id="entradaDatoX", type='number'),
        html.H4("Coordenada Y:"),
        dcc.Input(id="entradaDatoY", type='number'),
        html.Br(),
        dbc.Button('Enviar', id='button-send'),
        html.Br(),
        html.Label(id="salidaOk"),
    ]),
    
    #FIND ALL
    html.Div([
        html.H1("RESULTADOS TABLA - SENSOR 1"),
        dash_table.DataTable(
            id="resultadosSensor1",
            columns=[
                {'name':'Distancia','id':'Distancia','editable':False},
                {'name':'Create','id':'Create','editable':False},
                {'name':'Update','id':'Update','editable':False},
            ],
            data=readSensor()
        )
    ]),
    
    #Find One
    html.Div([
        html.H1("RESULTADO ÚNICO"),
        html.H4("buscar sensor:"),
        dcc.Input(id="valorBuscado", type='text'),
        html.Div([
            html.Label("Coordenada X:"),
            html.Label(id="coordenadaX"),
        ]),
        html.Div([
            html.Label("Coordenada Y:"),
            html.Label(id="coordenadaY"),
        ]),
        html.Div([
            html.Label(id="mensajeResultado"),  # Nuevo html.Label para el mensaje de resultado
        ]),
        html.Br(),
        dbc.Button('Enviar', id='buttonBuscado'),
    ])
        
])

#CREAR
@app.callback(
    Output('salidaOk','children'),
    Input('button-send','n_clicks'),
    State('entradaDatoX','value'),
    State('entradaDatoY','value'),
)
def entradaCoordenadas(n_clicks,entradaDatoX,entradaDatoY):
    if n_clicks is None:
        raise PreventUpdate
    
    if entradaDatoX is None or entradaDatoY is None:
        return "Ingrese los valores válidos para las coordenadas"   
    
    return createCoordenada(entradaDatoX,entradaDatoY)


#Find One
@app.callback(
    Output('coordenadaX', 'children'),
    Output('coordenadaY', 'children'),
    Output('mensajeResultado', 'children'),
    Input('buttonBuscado', 'n_clicks'),
    State('valorBuscado', 'value'),
    
)
def buscarUnValor(n_clicks,valorBuscado):
    if n_clicks is None:
        raise PreventUpdate
    
    if valorBuscado is None:
        return "Ingrese un valor", "", ""   
    
    coordenadas = readSensorUnico(valorBuscado)
    
    # Comprobar si se encontró un resultado
    if isinstance(coordenadas, tuple):
        coordenada_X, coordenada_Y = coordenadas
        return coordenada_X, coordenada_Y, ""
    
    else:
        return "", "", "No se encontró resultado"
    


if __name__ == "__main__":
    app.run_server(debug=True)