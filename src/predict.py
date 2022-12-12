import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
img = html.Img(src=r'assets/demo_scatter_plot.png', alt='image', style={'height':'50%', 'width':'50%'})

df = pd.DataFrame(
    {
        "Model Name": ["A Model", "B Model", "C Model"],
        "train_r2_score": [0.5, 0.5, 0.5],
        "test_r2_score": [0.5, 0.5, 0.5],
        "train_RMSE": [0.5, 0.5, 0.5],
        "test_RMSE": [0.5, 0.5, 0.5],
        "train_MAE": [0.5, 0.5, 0.5],
        "test_MAE": [0.5, 0.5, 0.5],
        "scatter plot": [img, img, img],
    }
)

predict_layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H2("Prediction Models...")
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="primary")
        ], width=12),
    ])
])


