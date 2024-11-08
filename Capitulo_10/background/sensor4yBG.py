from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

def create_figure_S4Y(x_data, y_data):
    return {
        'data': [
            go.Scatter(
                x=x_data,
                y=y_data,
                mode='lines+markers',
                marker={'size': 5},
            )
        ],
        'layout': go.Layout(
            xaxis={
                'title': {
                    'text': 'Tiempo',  # Título del eje X
                    'font': {'size': 8}  # Ajusta el tamaño del texto del título del eje X
                },
                'tickfont': {'size': 10},  # Ajusta el tamaño del texto de las etiquetas del eje X
                'tickvals': x_data,  # Asegúrate de mostrar todas las etiquetas de los valores de x_data
            
            },
            yaxis={
                'title': {
                    'text': 'Aceleracion en Y',  # Título del eje Y
                    'font': {'size': 8}  # Ajusta el tamaño del texto del título del eje Y
                },
                'tickfont': {'size': 10},  # Ajusta el tamaño del texto de las etiquetas del eje Y
            },
            margin=dict(l=30, r=0, b=50, t=0),  # Ajustar márgenes si es necesario
            height=150,  # Ajustar la altura del gráfico
        )
    }

sensorDistancia1 = dbc.Container([
    html.Label("Sensor 4 - Acelerómetro en Y"),
    dcc.Graph(id="sensorAceY", figure=create_figure_S4Y([], [])),
    dcc.Interval(id='interval-sensorAceY', interval=2000, n_intervals=0),
])
