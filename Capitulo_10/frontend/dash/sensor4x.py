from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Datos de ejemplo
data = [1, 2, 3, 4, 5]
tiempo = [10, 15, 13, 17, 21]

sensor4x = dbc.Container([
    html.Label("Sensor 4 - Acelerómetro en X"),
    dcc.Graph(id="sensorAceX"),
    dcc.Interval(
        id='interval-sensorAceX',
        interval=2000,
        n_intervals=0
    ),
])