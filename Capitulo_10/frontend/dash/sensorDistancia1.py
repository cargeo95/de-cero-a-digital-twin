from dash import html,dcc
import dash_bootstrap_components as dbc

sensorDistancia1 = dbc.Container([
    html.Label("Sensor - Distancia 1"),
    dcc.Graph(id="sensorDistancia1"),
    dcc.Interval(
        id='interval-sensorDistancia1',
        interval=2000,
        n_intervals=0
    ),
])