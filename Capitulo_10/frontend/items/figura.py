from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

#impor predict
from .predict import predict

#conexión base de datos
from bd.ubicacionController import readSensor
lectura = readSensor()

# Extraer coordenadas
nombres = [i['nombre'] for i in lectura]
coordenada_X = [i['coordenada_X'] for i in lectura]
coordenada_Y = [i['coordenada_Y'] for i in lectura]
coordenada_Z = [i['coordenada_Z'] for i in lectura]

# Coordenadas punto Lechada
coordenada_lechada_X = [1, 4, 3]
coordenada_lechada_Y = [5, 2, 6]
coordenada_lechada_Z = [1, 1, 1]
nombres_lechada = ['Lechada 1', 'Lechada 2', 'Lechada 3']

# Crear las anotaciones para cada punto
annotations = []
for x, y, z, nombre in zip(coordenada_X +coordenada_lechada_X ,
                           coordenada_Y + coordenada_lechada_Y, 
                           coordenada_Z +coordenada_lechada_Z, 
                           nombres + nombres_lechada):
    annotations.append(
        dict(
            x=x,
            y=y,
            z=z,
            text=nombre,
            xanchor='left',
            showarrow=False,
            font=dict(
                size=12,
                color='black'
            )
        )
    )

figura = dbc.Container([
    html.H4("Mapa sensores"),
    html.Br(),
    dcc.Graph(
        id="coordenadas_sensores",
        figure={
            'data' :[
                go.Scatter3d(
                    x = coordenada_X,
                    y = coordenada_Y,
                    z =  coordenada_Z,
                    mode='markers',
                    marker = {'size':5},
                    text=nombres,  # Añadir nombres para el hover
                    name='Ubicación sensor',
                    textposition='top right'  # Posición de los textos
                ),
                go.Scatter3d(
                    x=coordenada_lechada_X,
                    y=coordenada_lechada_Y,
                    z=coordenada_lechada_Z,
                    mode='markers',
                    marker={'size': 5, 'color': 'red'},
                    text=nombres_lechada,
                    name='Punto Lechada',
                    textposition='top right'  # Posición de los textos
                )
            ],
            'layout': go.Layout(
                title={
                    'text': 'Ubicación Geoespacial',
                    'x': 0.5,  # Centrar el título
                    'xanchor': 'center'
                },
                margin=dict(l=0, r=0, b=0, t=30),  # Ajustar márgenes, dejar un poco de espacio para el título
                scene=dict(
                    annotations=annotations
                ),
                legend=dict(
                    orientation="h",  # Horizontal
                    yanchor="top",
                    y=-0.1,  # Posicionar la leyenda debajo de la gráfica
                    xanchor="center",
                    x=0.5
                )
            )
        }
        
    ),
    html.Br(),
    predict
    
    
])