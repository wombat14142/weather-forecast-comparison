# app.py
import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
