from dash import html, dcc
import dash_bootstrap_components as dbc


centro = dbc.Container(
    [
        html.H1('TEXTO CENTRO'),
        html.H2('Realizaremos las operaciones matemáticas básicas'),
        #cálculo matemático para un circulo:
        html.Div([
            html.Label('Area del circulo '),
            dcc.Input(id = 'entradaCirculo', value = 5 , type = 'number'),
            html.Label(id = 'salidaCirculo'),
        ]),
        
        #área de un triangulo:
        html.Div(
            [
                html.Label('Area del Triangulo '),
                dcc.Input(id = 'entradaBaseTriangulo', value = 5 , type = 'number'),
                dcc.Input(id = 'entradaAlturaTriangulo', value = 5 , type = 'number'),
                html.Label(id = 'salidaTriangulo'),
            ]
        ),
        
        html.Hr(),
        
        #Operación matemática cualquiera que sea
        html.Div([
            html.Label('Entrada de un valor:'),
            dcc.Input(id = 'entradaValor', value = 5 , type = 'number'),
            html.Label(id = 'salidaValor'),
        ]),
        
        

    ]
)