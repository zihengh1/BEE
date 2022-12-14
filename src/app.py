import pathlib
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
from predict import predict_layout
from customize import customize_layout
from classification import classification_layout
# from appServer import app

# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("data").resolve()
app = Dash(__name__, 
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            suppress_callback_exceptions=True,
            meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
            )
server = app.server
app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Framework", tab_id="tab-framework", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Regression", tab_id="tab-regression", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Online Prediction", tab_id="tab-customize", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            ],
            id="tabs",
            active_tab="tab-framework",
        ),
    ], className="mt-3"
)

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("CS765 Project - Predictor",
                            style={"textAlign": "center"}), width=12)),
    html.Hr(),
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"),
    html.Div(id='content', children=[])

])

@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-regression":
        return classification_layout
    elif tab_chosen == "tab-framework":
        return predict_layout
    elif tab_chosen == "tab-customize":
        return customize_layout
    return html.P("This shouldn't be displayed for now...")



if __name__=='__main__':
    app.run_server(debug=False, host = "0.0.0.0", port=15006)
