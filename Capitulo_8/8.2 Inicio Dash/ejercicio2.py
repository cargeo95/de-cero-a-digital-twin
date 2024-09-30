#https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

#https://dash-bootstrap-components.opensource.faculty.ai/examples/

import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

miVariable = dbc.Card(
    [
        dbc.CardHeader("Header"),
        dbc.CardBody(
            [
                html.H5("Soy un título", className="card-title"),
                html.P(
                    "Aparezco con el texto de la card",
                    className="card-text",
                ),
                dbc.Button("Soy un button", color="primary"),
            ]
        )
    ]
)

app.layout = dbc.Container(
    [  
        html.H1('Hello World'),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col('Texto 1', md=6 , style={'background-color':'blue'} ),
                dbc.Col('Texto 2', md=6, style={'background-color':'red'}),
                dbc.Col(miVariable, md=12, style={'background-color':'green'}),
            ],
            align="center",
        )
    ],
    fluid=True
)



if __name__ == '__main__':
    app.run_server(debug=True)