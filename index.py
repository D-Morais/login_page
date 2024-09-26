import dash_bootstrap_components as dbc
from dash import html, dcc, no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from pages import login, page_exemplo
from app import app
from utils import encrypt, login_user


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='session', storage_type='session'),
    html.Div(id='page-content'),
    html.Div(id='login-out', className="mt-1")
])


@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname'),
        Input('session', 'data')
    ]
)
def display_page(pathname, user_data):
    if not user_data:
        return login.layout

    if pathname == '/page_exemplo':

        if user_data:
            return page_exemplo.layout(user_data)

        return login.layout

    else:
        return login.layout


@app.callback(
    [
        Output('session', 'data'),
        Output('url', 'pathname'),
        Output('login-out', 'children')
    ],
    Input('access', 'n_clicks'),
    [
        State('user', 'value'),
        State('password', 'value')
    ]
)
def verify_login(n_clicks, username, password):
    if n_clicks:
        if not username or not password:
            return None, no_update, dbc.Alert("Usuário ou senha não informados!", color="danger", is_open=True,
                                              duration=2000, style={"width": "33%", "margin-left": "33%"})

        user = login_user(username, password)

        if user:
            return user, '/page_exemplo', no_update

        return None, no_update, dbc.Alert("Usuário ou senha incorretos!", color="danger", is_open=True, duration=2000)

    else:
        return no_update


if __name__ == '__main__':
    app.run_server(debug=True)
