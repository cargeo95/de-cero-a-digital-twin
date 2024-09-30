from dash import Dash, html,dcc, callback, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#importamos back
from backend.calculoinundacion import consultarDepartamento, departamentos

print(departamentos)

#App layout
app.layout = dbc.Container(
    [
        html.H1("Colegios inundados con un buffer de 50"),
        dcc.Dropdown(departamentos['DeNombre'].unique(), 'Cundinamarca' , id='departamento_consultado'),
        dcc.Graph(
            id="mapa",
            style={
                'width': '100%', 
                "height": "600px"
                },
        )
        
    ],
    fluid=True
)

@callback(
    Output("mapa", "figure"),
    Input("departamento_consultado", "value")
)

def update_map(departamento_consultado):
    return consultarDepartamento(departamento_consultado)


if __name__ == "__main__":
    app.run_server(debug=True)