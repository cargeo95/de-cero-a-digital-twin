from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Datos de ejemplo
data = [1, 2, 3, 4, 5]
tiempo = [10, 15, 13, 17, 21]

sensorV2 = dbc.Container([
    html.Label("Sensor 2 - Vibración"),
    dcc.Graph(id="sensorVibracion2"),
    dcc.Interval(
        id='interval-sensorVibracion2',
        interval=2000,
        n_intervals=0
    ),
])