from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__)


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    # create a button with boostrap
    html.Button('Click me', id='button', className='btn btn-primary'),

    # create a input with boostrap
    html.Div([
        html.Label('Soy un titulo para el input'),
        dcc.Input(id='input', type='text', value='4654654564')
    ], className='form-group'),

    

])

if __name__ == '__main__':
    app.run_server(debug=True)
