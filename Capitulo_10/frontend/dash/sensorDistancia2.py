from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Datos de ejemplo
data = [1, 2, 3, 4, 5]
tiempo = [10, 15, 13, 17, 21]

sensorDistancia2 = dbc.Container([
    html.Label("Sensor - Distancia 2"),
    dcc.Graph(id="sensorDistancia2"),
    dcc.Interval(
        id='interval-sensorDistancia2',
        interval=2000,
        n_intervals=0
    ),
])