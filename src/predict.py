import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

img = html.Img(src=r'assets/demo_scatter_plot.png', alt='image', style={'height':'50%', 'width':'50%'})

performance_df = pd.DataFrame(
    {
        "Model Name": ["Ridge", "Lasso", "Random Forest"],
        "R-Squared Score (Train)": [0.5, 0.5, 0.5],
        "R-Squared Score (Test)": [0.5, 0.5, 0.5],
        "RMSE (Train)": [0.5, 0.5, 0.5],
        "RMSE (Test)": [0.5, 0.5, 0.5],
        "MSE (Train)": [0.5, 0.5, 0.5],
        "MSE (Test)": [0.5, 0.5, 0.5],
        "Scatter plot": [img, img, img],
    }
)

predict_layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H2("Regression Models...")
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Table.from_dataframe(performance_df, striped=True, bordered=True, hover=True, color="primary")
        ], width=12),
    ])
])


