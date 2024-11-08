from dash import html,dcc
import dash_bootstrap_components as dbc

predict = dbc.Container([
    html.H4("Predicción de lechada"),
    html.Label("Realizar inyección de lechada en:"),
    dbc.Row([
        dbc.Col(
            html.Label("¡¡¡ Inyección 1!!!"),
            md=4,
            style={'background-color':'red',
                   'color':'white'
                }
        ),
        dbc.Col(
            html.Label("¡¡¡ Inyección 2!!!"),
            md=4,
            style={'background-color':'white'}
        ),
        dbc.Col(
            html.Label("¡¡¡ Inyección 3!!!"),
            md=4,
            style={'background-color':'white'}
        ),
        
    ])
])