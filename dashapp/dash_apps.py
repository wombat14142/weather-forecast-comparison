# dashapp/dash_apps.py

from dash import Dash, html
from django_plotly_dash import DjangoDash  # Import DjangoDash instead of Dash

# Create a Dash app instance
app = DjangoDash('SimpleDashboard')

# Define layout for the Dash app
app.layout = html.Div([
    html.H1('Hello from Dash inside Django!'),
    html.P('This is a simple Dash app integrated into Django.')
])
