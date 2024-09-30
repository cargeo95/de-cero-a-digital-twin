import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[    
        html.H1('Hello World'),
        html.H2('Empezaré mi primer código de dash'),
        html.H3('Simplemente recuerdo que tengo diferentes tamaños'),
        html.Label('O que también existen los label'),
        html.Br(),html.Br(),html.Br(),
        html.Label('así como los saltos de línea'),
        html.Br(),html.Br(),html.Br(),
        dcc.Input(type='text', value="el valor que quiera aparecer", id="entrada"),
        dcc.Dropdown(
            ['Opción 1', 'Opción 2', 'Opción 3']
        ),
        dcc.Dropdown(
            ['Opción 1', 'Opción 2', 'Opción 3'],
            value = 'Opción 1'
        ),
        dcc.Dropdown(
            ['Opción 1', 'Opción 2', 'Opción 3'],
            value='Opción 1',
            multi=True
        ),
        dcc.RadioItems(
            ['Opción 1', 'Opción 2', 'Opción 3']
        ),
        dcc.RadioItems(
            ['Opción 1', 'Opción 2', 'Opción 3'],
            value='Opción 1'
        ),
        dcc.Checklist(
            ['Opción 1', 'Opción 2', 'Opción 3'],
        ),
        dcc.Slider(
            min=0,
            max=10,
            step=1,
            value=5
        )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)