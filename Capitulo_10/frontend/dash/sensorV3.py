from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Datos de ejemplo
data = [1, 2, 3, 4, 5]
tiempo = [10, 15, 13, 17, 21]

sensorV3 = dbc.Container([
    html.Label("Sensor 3 - Vibración Sensible"),
    dcc.Graph(id="sensorVibracion3"),
    dcc.Interval(
        id='interval-sensorVibracion3',
        interval=2000,
        n_intervals=0
    ),
])