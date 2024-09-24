import dash
from dash.exceptions import PreventUpdate
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import *
from utils import encrypt, create_user

layout = dbc.Container([

    # ========= Seleção de Perfil ========= #
    dbc.Card([
        dbc.Row([
            html.H1("Login", className="text-primary",
                    style={"text-align": "center", "color": "blue", "margin-top": "30px"}),
            html.Div(style={"height": "40px"}),
        ]),
        dbc.FormFloating([
            dbc.Input(type="text", placeholder="Digite seu usuário", id="usuario"),
            dbc.Label("Usuário")
        ], style={"margin": "15px"}),
        dbc.FormFloating([
            dbc.Input(type="password", placeholder="Digite sua senha", id="senha"),
            dbc.Label("Senha")
        ], style={"margin": "15px"}),
        dbc.Row([
            dbc.Button("Acessar", color="primary", id="acessar", style={"width": "25%"}, n_clicks=0),
            dbc.Button("Novo Usuário", color="success", id="novo_usuario", style={"width": "30%"}, n_clicks=0)
        ], style={"margin": "15px", "flex-direction": "row", "justify-content": "space-between"}),
        html.Div(id="login-output", className="mt-2")
    ], style={"width": "40%", "margin-top": "60px", "background-color": "#f1f1f1"}),

    dbc.Card([
        html.Div([
            dbc.Row([
                html.Span('x', id='close-modal', className='close', style={"margin-left": "5px"}),
                html.H2("Cadastrar usuário", className="text-primary", style={"text-align": "center", "color": "blue",
                                                                              "margin-top": "30px"}),
                html.Div(style={"height": "40px"})
            ]),
            dbc.FormFloating([
                dbc.Input(type="text", placeholder="", id="reg-usuario"),
                dbc.Label("Novo usuário")
            ], style={"margin": "15px"}),
            dbc.FormFloating([
                dbc.Input(type="password", placeholder="", id="reg-senha"),
                dbc.Label("Escolha sua senha")
            ], style={"margin": "15px"}),
            dbc.FormFloating([
                dbc.Input(type="email", placeholder="", id="reg-email"),
                dbc.Label("Insira seu e-mail")
            ], style={"margin": "15px"}),
            dbc.Button("Adicionar", color="primary", id="adc-usuario",
                       style={"width": "30%", "display": "block", "margin": "auto auto"},
                       n_clicks=0),
            html.Div(id='reg-output-state', className="mt-2")
        ], style={"width": "33%", "height": "80%", "margin-left": "34%", "margin-top": "60px", "border-radius": "5px",
                  "border": "1px solid rgba(0, 0, 0, 0.2)", "background-color": "#f1f1f1"}, className='modal-content')
    ], style={"width": "100%", "height": "100%", "border-radius": "5px"}, id='modal', className='modal')

], style={"width": "100%", "height": "100%", "border-radius": "5px", "display": "flex", "justify-content": "center"})


@app.callback(
    Output('modal', 'style'),
    [Input('novo_usuario', 'n_clicks'),
     Input('close-modal', 'n_clicks')],
    State('modal', 'style')
)
def toggle_modal(reg_clicks, close_clicks, current_style):
    if reg_clicks or close_clicks:
        if current_style and current_style.get('display') == 'flex':
            return {'display': 'none'}
        return {'display': 'flex'}
    return {'display': 'none'}


@app.callback(
    [
        Output('reg-output-state', 'children'),
        Output("reg-usuario", "value"),
        Output("reg-senha", "value"),
        Output("reg-email", "value")
    ],
    Input('adc-usuario', 'n_clicks'),
    [
        State('reg-usuario', 'value'),
        State('reg-senha', 'value'),
        State('reg-email', 'value')
    ],
)
def adc_novo_usuario(n_clicks, novo_usuario, nova_senha, novo_email):
    if n_clicks:

        if not novo_email or not novo_usuario or not nova_senha:
            return dbc.Alert("Necessário preencher todos os campos.", color="warning", is_open=True, duration=2000), \
                   novo_usuario, nova_senha, novo_email

        else:
            hash_senha = encrypt(nova_senha)
            message, color, return_user, return_password, return_email = create_user(novo_usuario, hash_senha,
                                                                                     novo_email)
            return dbc.Alert(f"{message}", color=color, is_open=True, duration=2000), \
                   return_user, return_password, return_email

    else:
        return dash.no_update
