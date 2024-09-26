import dash_bootstrap_components as dbc
from dash import html, no_update
from dash.dependencies import Input, Output, State

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
            dbc.Input(type="text", placeholder="Digite seu usuário", id="user"),
            dbc.Label("Usuário")
        ], style={"margin": "15px"}),
        dbc.FormFloating([
            dbc.Input(type="password", placeholder="Digite sua senha", id="password"),
            dbc.Label("Senha")
        ], style={"margin": "15px"}),
        dbc.Row([
            dbc.Button("Acessar", color="primary", id="access", style={"width": "25%"}, n_clicks=0),
            dbc.Button("Novo Usuário", color="success", id="new-user", style={"width": "30%"}, n_clicks=0)
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
                dbc.Input(type="text", placeholder="", id="reg-user"),
                dbc.Label("Novo usuário")
            ], style={"margin": "15px"}),
            dbc.FormFloating([
                dbc.Input(type="password", placeholder="", id="reg-password"),
                dbc.Label("Escolha sua senha")
            ], style={"margin": "15px"}),
            dbc.FormFloating([
                dbc.Input(type="email", placeholder="", id="reg-email"),
                dbc.Label("Insira seu e-mail")
            ], style={"margin": "15px"}),
            dbc.Button("Adicionar", color="primary", id="adc-user",
                       style={"width": "30%", "display": "block", "margin": "auto auto"},
                       n_clicks=0),
            html.Div(id='reg-output-state', className="mt-2")
        ], style={"width": "33%", "height": "80%", "margin-left": "34%", "margin-top": "60px", "border-radius": "5px",
                  "border": "1px solid rgba(0, 0, 0, 0.2)", "background-color": "#f1f1f1"}, className='modal-content')
    ], style={"width": "100%", "height": "100%", "border-radius": "5px"}, id='modal', className='modal')

], style={"width": "100%", "height": "100%", "border-radius": "5px", "display": "flex", "justify-content": "center"})


@app.callback(
    Output('modal', 'style'),
    [Input('new-user', 'n_clicks'),
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
        Output("reg-user", "value"),
        Output("reg-password", "value"),
        Output("reg-email", "value")
    ],
    Input('adc-user', 'n_clicks'),
    [
        State('reg-user', 'value'),
        State('reg-password', 'value'),
        State('reg-email', 'value')
    ],
)
def adc_novo_usuario(n_clicks, new_user, new_password, new_email):
    if n_clicks:

        if not new_email or not new_user or not new_password:
            return dbc.Alert("Necessário preencher todos os campos.", color="warning", is_open=True, duration=2000), \
                   new_user, new_password, new_email

        else:
            hash_password = encrypt(new_password)
            message, color, return_user, return_password, return_email = create_user(new_user, hash_password,
                                                                                     new_email)
            return dbc.Alert(f"{message}", color=color, is_open=True, duration=2000), return_user, return_password,\
                return_email

    else:
        return no_update
