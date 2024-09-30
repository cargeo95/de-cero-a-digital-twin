import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Store(id="store"),
    html.H1("A simple example"),
    html.Hr(),
    dbc.Button("Click me", id="button"),

    dbc.Tabs(
        [
            dbc.Tab(label="Tab 1", tab_id="tab-1"),
            dbc.Tab(label="Tab 2", tab_id="tab-2"),
        ],
        id="tabs",
        active_tab="tab-1",
    ),

    html.Div(id="tab-content", className="p-4"),

])


if __name__ == '__main__':
    app.run_server(debug=True)