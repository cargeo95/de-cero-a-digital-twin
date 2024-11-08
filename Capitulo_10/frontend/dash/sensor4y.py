from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Datos de ejemplo
data = [1, 2, 3, 4, 5]
tiempo = [10, 15, 13, 17, 21]

sensor4y = dbc.Container([
    html.Label("Sensor 4 - Acelerómetro en Y"),
    dcc.Graph(id="sensorAceY"),
    dcc.Interval(
        id='interval-sensorAceY',
        interval=2000,
        n_intervals=0
    ),
])