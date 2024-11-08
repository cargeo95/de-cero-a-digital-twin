from dash import html
import dash_bootstrap_components as dbc
from .items.figura import figura
from .dash.general import general

layout = dbc.Container([
        html.H1("Asentamiento estructura"),
        html.Hr(),
        dbc.Row([
            dbc.Col(figura, md=4),
            dbc.Col(general,md=8),
        ]),        
    ],
        style={
        'height': '100vh',
        'text-align': 'center',
        'justify-content': 'center',
        'align-items': 'center',
    }
    ,
    fluid=True
)