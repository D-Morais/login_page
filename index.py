from dash import html, dcc
from dash.dependencies import Input, Output
from pages import login, page_exemplo
from app import app


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='session', storage_type='session'),
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname'),
        Input('session', 'data')
    ]
)
def display_page(pathname, user_data):
    if pathname == '/page_exemplo':

        if user_data and user_data.get('logged_in'):
            return page_exemplo.layout

        return login.layout

    else:
        return login.layout


if __name__ == '__main__':
    app.run_server(debug=True)
