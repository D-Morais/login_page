from dash import html, dcc


def layout(user_data):
    return html.Div([
        html.H2("Página 1"),
        html.P(f"Conteúdo específico para {user_data}."),
        html.Br(),
        dcc.Link('Voltar para a página inicial', href='/')
    ])
