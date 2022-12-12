from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
app = Dash(__name__, 
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            suppress_callback_exceptions=True,
            meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
            )
server = app.server