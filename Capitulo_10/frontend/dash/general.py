from dash import html,dcc
import dash_bootstrap_components as dbc

#importamos sensores
from .sensorV1 import sensorV1
from .sensorV2 import sensorV2
from .sensorV3 import sensorV3
from .sensor4x import sensor4x
from .sensor4y import sensor4y
from .sensorDistancia1 import sensorDistancia1
from .sensorDistancia2 import sensorDistancia2

# Define estilos adicionales en CSS
styles = {
    'column-style': {
        'height': '190px',  # Ajusta la altura deseada
        'padding': '5px',  # Ajusta el padding deseado
        'border': '1px solid #ddd'  # Solo para visualizar los bordes de las columnas
    }
}

general = dbc.Container([
    html.H4("Visualización sensores"),
    html.Br(),
    dbc.Row([
        dbc.Col(sensorV1,md=4,style=styles['column-style']),
        dbc.Col(sensorV2,md=4,style=styles['column-style']),
        dbc.Col(sensorV3,md=4,style=styles['column-style']),
        dbc.Col(sensor4x,md=6,style=styles['column-style']),
        dbc.Col(sensor4y,md=6,style=styles['column-style']),
        dbc.Col(sensorDistancia1,md=6,style=styles['column-style']),
        dbc.Col(sensorDistancia2,md=6,style=styles['column-style']),
    ])
])