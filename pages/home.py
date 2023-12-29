import dash
from dash import html

dash.register_page(__name__, path='/', title="Home", image="Image1.jpg", description="This is Home page")

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
])