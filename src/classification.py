import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc

img_sc = html.Img(src=r'assets/demo_scatter_plot.png', alt='image', style={'height':'50%', 'width':'50%'})
img_li = html.Img(src=r'assets/demo_scatter_plot.png', alt='image', style={'height':'50%', 'width':'50%'})
df_scatter = pd.DataFrame(
    {
        "Model Name": ["A Model", "B Model", "C Model"],
        "accurancy_score": [0.5, 0.5, 0.5],
        "precision_score": [0.5, 0.5, 0.5],
        "recall_score": [0.5, 0.5, 0.5],
        "f1": [0.5, 0.5, 0.5],
        "confusion matrix": [img_sc, img_sc, img_sc],
    }
)
df_line = pd.DataFrame(
    {
        "Model Name": ["D Model", "E Model", "F Model"],
        "accurancy_score": [0.1, 0.1, 0.1],
        "precision_score": [0.1, 0.1, 0.1],
        "recall_score": [0.1, 0.1, 0.1],
        "f1": [0.1, 0.1, 0.1],
        "confusion matrix": [img_li, img_li, img_li],
    }
)

classification_layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H2("Prediction Models...")
        ], width=12),
        
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="attr",
                options=[
                    {"label": "Age", "value": "age"},
                    {"label": "Status", "value": "status"},
                    {"label": "Jobs", "value": "jobs"}],
                multi=False,
                value="age",
                clearable=False,
                style={'width': "40%", 'float':'right'},
                className='form-dropdown',
                ),
        ], width = 12),
    ], className='mb-4'),
    # dbc.Row([
    #     dbc.Col([
    #         dbc.Table.from_dataframe(df, id="table", striped=True, bordered=True, hover=True, color="primary")
    #     ], width=12),
    # ]),
    dbc.Row([
        dbc.Col(id="table", width=12),
    ]),
    
])

@callback(
    Output(component_id='table', component_property='children'),
    [Input(component_id='attr', component_property='value')]
)
def update_graph(option_atr):
    if option_atr == "age":
        print(df_scatter)
        return dbc.Table.from_dataframe(df_scatter, striped=True, bordered=True, hover=True, color="primary")
    if option_atr == "status":
        print(df_line)
        return dbc.Table.from_dataframe(df_line, striped=True, bordered=True, hover=True, color="success")


