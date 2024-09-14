from dash.exceptions import PreventUpdate
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


layout = dbc.Container([
    # ========= Seleção de Perfil ========= #
    dbc.Card([
        html.H1("Login", className="text-primary",
                style={"text-align": "center", "color": "blue", "margin-top": "20px"}),
        html.Hr(),
        html.Div(style={"height": "40px"}),
        dbc.FormFloating([
            dbc.Input(type="text", placeholder="Digite seu usuário", id="usuario", style={"border-radius": "5px"}),
            dbc.Label("Usuário")
        ], style={"margin": "15px"}),
        dbc.FormFloating([
            dbc.Input(type="password", placeholder="Digite sua senha", id="senha", style={"border-radius": "5px"}),
            dbc.Label("Senha")
        ], style={"margin": "15px"}),
        dbc.Row([
            dbc.Button("Acessar", color="primary", id="acessar", style={"width": "25%"}, n_clicks=0),
            dbc.Button("Novo Usuário", color="success", id="novo_usuario", style={"width": "30%"}, n_clicks=0)
        ], style={"margin": "15px", "flex-direction": "row", "justify-content": "space-between"}),
        html.Div(id="login-output", className="mt-2")
    ], style={"width": "40%", "margin-top": "60px", "background-color": "#f1f1f1"}),

    # Modal
    html.Div([
        html.Div([
            html.Span('x', id='close-modal', className='close', style={"margin-left": "5px"}),
            html.H2("Cadastrar usuário", className="text-primary", style={"text-align": "center", "color": "blue",
                                                                          "margin-top": "10px"}),
            html.Hr(),
            dbc.CardImg(src="/assets/img_hom.png", alt="Avatar", className='perfil_avatar'),
            html.Hr(),
            dbc.FormFloating([
                dbc.Input(type="text", placeholder="", id="reg_usuario", style={"border-radius": "5px"}),
                dbc.Label("Novo usuário")
            ], style={"margin": "10px 20px"}),
            dbc.FormFloating([
                dbc.Input(type="password", placeholder="", id="reg_senha", style={"border-radius": "5px"}),
                dbc.Label("Escolha sua senha")
            ], style={"margin": "10px 20px", "border-radius": "5px"}),
            dbc.Button("Adicionar", color="primary", id="adc_usuario",
                       style={"border-radius": "5px", "width": "30%", "display": "block", "margin": "0 auto"},
                       n_clicks=0),
            html.Div(id='reg-output-state')
        ], style={"width": "40%", "height": "90%", "margin-left": "30%", "margin-top": "30px", "border-radius": "5px",
                  "background-color": "#f1f1f1"}, className='modal-content')
    ], id='modal', className='modal')

], style={"width": "100%", "height": "100%", "border-radius": "5px", "display": "flex", "justify-content": "center"})
