import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from pages import login, page_exemplo


app = Dash(__name__, suppress_callback_exceptions=True, title="Sistema de Login", external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='session', storage_type='session'),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page_exemplo':
        return page_exemplo.layout
    else:
        return login.layout


if __name__ == '__main__':
    app.run_server(debug=True)
