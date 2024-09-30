import dash
from dash import html
import dash_bootstrap_components as dbc

#importamos estructura
from .estructura.izquierda import izquierda
from .estructura.centro import centro
from .estructura.derecha import derecha


layout = dbc.Container(
    [
                dbc.Row(
            [
                dbc.Col(izquierda, md=3, style={'background-color':'red'}),
                dbc.Col(centro, md=6,style={'background-color':'white'}),
                dbc.Col(derecha, md=3, style={'background-color':'green'}),

            ]
        )
    ]
)