import dash_bootstrap_components as dbc
from dash import Dash


app = Dash(__name__, suppress_callback_exceptions=True, title="Sistema de Login", external_stylesheets=[dbc.themes.BOOTSTRAP])
app.scripts.config.serve_locally = True
server = app.server
