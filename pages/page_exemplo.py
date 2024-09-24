import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import html
from dash.dependencies import Input, Output, State

from app import app

layout = dbc.Container([
    html.H2("Página 1 - Informações do Usuário"),
    html.Div(id='info-usuario-pagina1'),
    html.Br(),
    html.A('Sair', href='/login')
])
