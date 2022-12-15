import math
import pickle
import pathlib
import numpy as np
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State, callback  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc

prediction_layout = html.Div(
    [
        dbc.Alert(
            "Total amount of time should not over 1440",
            id="alert-fade",
            dismissable=True,
            is_open=False,
            color="danger",
        ),
        dbc.Row(
            [
                dbc.Row(
                    [
                        html.P("Total time:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em'}),
                        html.P(id="total_time", style={'font':'Monospace','color':'#66B3FF', 'font-size':'1.5em', 'text-decoration':'underline'}),
                    ]
                ),
                dbc.Col(
                    [
                        
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("01 Personal Care Activities"),
                                        html.Br(),
                                        html.Br(),
                                        dcc.Slider(
                                            min=0, 
                                            max=1440, 
                                            step=144, 
                                            value=144,
                                            tooltip={"always_visible":False, "placement":"bottom"},
                                            updatemode='drag',
                                            id='slider_1'
                                        ),
                                    ],
                                ),
                                dbc.Col(
                                    [
                                        html.Label("12 Socializing, Relaxing, and Leisure"),
                                        html.Br(),
                                        html.Br(),
                                        dcc.Slider(
                                            min=0, 
                                            max=1440, 
                                            step=144, 
                                            value=144,
                                            tooltip={"always_visible":False, "placement":"bottom"},
                                            updatemode='drag',
                                            id='slider_2'
                                        ),
                                    ],
                                ),
                            ],
                            className="mt-4",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("05 Work & Work-Related Activities"),
                                        html.Br(),
                                        html.Br(),
                                        dcc.Slider(
                                            min=0, 
                                            max=1440, 
                                            step=144, 
                                            value=144,
                                            tooltip={"always_visible":False, "placement":"bottom"},
                                            updatemode='drag',
                                            id='slider_3'
                                        ),
                                    ],
                                ),
                                dbc.Col(
                                    [
                                        html.Label("02 Household Activities"),
                                        html.Br(),
                                        html.Br(),
                                        dcc.Slider(
                                            min=0, 
                                            max=1440, 
                                            step=144, 
                                            value=144,
                                            tooltip={"always_visible":False, "placement":"bottom"},
                                            updatemode='drag',
                                            id='slider_4'
                                        ),
                                    ],
                                ),
                            ],
                            className="mt-4",
                        ), 
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("18 Traveling"),
                                        html.Br(),
                                        html.Br(),
                                        dcc.Slider(
                                            min=0, 
                                            max=1440, 
                                            step=144, 
                                            value=144,
                                            tooltip={"always_visible":False, "placement":"bottom"},
                                            updatemode='drag',
                                            id='slider_5'
                                        ),
                                    ],
                                ),
                                dbc.Col(
                                    [
                                        html.Label("11 Eating and Drinking"),
                                        html.Br(),
                                        html.Br(),
                                        dcc.Slider(
                                            min=0, 
                                            max=1440, 
                                            step=144, 
                                            value=144,
                                            tooltip={"always_visible":False, "placement":"bottom"},
                                            updatemode='drag',
                                            id='slider_6'
                                        ),
                                    ],
                                ),
                            ],
                            className="mt-4",
                        ),  
                    ],
                    width=8,
                ),
                dbc.Col(
                    [
                        dcc.Graph(id="input_plot", figure={})  
                    ]
                )
            ],
            className="mt-4",
        ),
        html.Img(id='age'),
        html.Img(id='childNum'),
        html.Img(id='childAge'),
        html.Img(id='workHours'),
        dcc.Store(id='age_pred', data=[], storage_type='memory'),
        dcc.Store(id='childNum_pred', data=[], storage_type='memory'),
        dcc.Store(id='childAge_pred', data=[], storage_type='memory'),
        dcc.Store(id='workHours_pred', data=[], storage_type='memory'),
    ]
)

@callback(
    Output(component_id="input_plot", component_property="figure"),
    Input(component_id="slider_1", component_property="value"),
    Input(component_id="slider_2", component_property="value"),
    Input(component_id="slider_3", component_property="value"),
    Input(component_id="slider_4", component_property="value"),
    Input(component_id="slider_5", component_property="value"),
    Input(component_id="slider_6", component_property="value"),
)

def generate_input_plot(input_1, input_2, input_3, input_4, input_5, input_6):
    pie = px.pie(values=[input_1,input_2,input_3,input_4,input_5,input_6], names=["T1", "T2", "T3", "T4", "T5", "T6"])
    return pie

@callback(
    Output("alert-fade", "is_open"),
    Output("total_time", component_property="children"),
    Input(component_id="slider_1", component_property="value"),
    Input(component_id="slider_2", component_property="value"),
    Input(component_id="slider_3", component_property="value"),
    Input(component_id="slider_4", component_property="value"),
    Input(component_id="slider_5", component_property="value"),
    Input(component_id="slider_6", component_property="value"),
    [State("alert-fade", "is_open")],
)
def toggle_alert_no_fade(input_1, input_2, input_3, input_4, input_5, input_6, is_open):
    total = input_1 + input_2 + input_3 + input_4 + input_5 + input_6
    if total > 1440:
        return True, total
    else :
        return False, total

@callback(
    Output("age_pred", component_property="data"),
    Output("childNum_pred", component_property="data"),
    Output("childAge_pred", component_property="data"),
    Output("workHours_pred", component_property="data"),
    Input(component_id="slider_1", component_property="value"),
    Input(component_id="slider_2", component_property="value"),
    Input(component_id="slider_3", component_property="value"),
    Input(component_id="slider_4", component_property="value"),
    Input(component_id="slider_5", component_property="value"),
    Input(component_id="slider_6", component_property="value"),
)
def online_prediction(input_1, input_2, input_3, input_4, input_5, input_6):
    output_attributes = ["TEAGE", "TRCHILDNUM", "TRYHHCHILD", "TEHRUSLT"]
    scaler_name = ["t01", "t12", "t05", "t02", "t18", "t11"]
    
    inputs = [input_1, input_2, input_3, input_4, input_5, input_6]
    
    avg_residual = 0
    if sum(inputs) < 1440:
        residual = 1440 - sum(inputs)
        avg_residual = residual / 6
        
    transform_inputs = []
    for i, input_value in enumerate(inputs):
        input_value += avg_residual
        scaler_path_name = "./saved_scaler/" + scaler_name[i] + ".pkl"
        with open(scaler_path_name, 'rb') as f:
            scaler = pickle.load(f)
        transformed_input = scaler.transform(np.expand_dims(np.array([input_value]), axis=1))
        transform_inputs.append(transformed_input[0])
    model_inputs = np.array(transform_inputs).T
    
    
    predictions = []
    for attr in output_attributes:
        model_path_name = "./saved_model/" + attr + "_mlp.pkl"
        with open(model_path_name, 'rb') as f:
            best_model = pickle.load(f)
        prediction = best_model.predict(model_inputs)
        if prediction[0] < 0:
            prediction[0] = 0
        predictions.append(prediction[0])

    return predictions[0],predictions[1],predictions[2],predictions[3]

@callback(
    Output("age", component_property="src"),
    Input("age_pred", component_property="data"),
)
def generate_age_figure(age):
    print(age)
    if age > 0 and age < 10 or age == 0:
        return "assets/age/baby.png"
    elif age >= 10 and age < 20:
        return "assets/age/teenager.png"
    elif age >= 20 and age < 40:
        return "assets/age/adult.png"
    elif age >= 40 and age < 60:
        return "assets/age/oldAdult.png"
    else:
        return "assets/age/elder.png"

# @callback(
#     Output("childNum", component_property="src"),
#     Input("childNum_pred", component_property="data"),
# )
# def generate_age_figure(ch):
#     childNum = math.ceil(ch)
#     if childNum == 0 and childNum == 1:
#         return "assets/infant_1.png"
#     else:
#         return "assets/infant_2.png"
# @callback(
#     Output("age", component_property="src"),
#     Input("age_pred", component_property="data"),
# )
# def generate_age_figure(age):
#     print(age)
#     if age > 0 and age < 10 or age == 0:
#         return "assets/age/baby.png"
#     elif age >= 10 and age < 20:
#         return "assets/age/teenager.png"
#     elif age >= 20 and age < 40:
#         return "assets/age/adult.png"
#     elif age >= 40 and age < 60:
#         return "assets/age/oldAdult.png"
#     else:
#         return "assets/age/elder.png"
# @callback(
#     Output("age", component_property="src"),
#     Input("age_pred", component_property="data"),
# )
# def generate_age_figure(age):
#     print(age)
#     if age > 0 and age < 10 or age == 0:
#         return "assets/age/baby.png"
#     elif age >= 10 and age < 20:
#         return "assets/age/teenager.png"
#     elif age >= 20 and age < 40:
#         return "assets/age/adult.png"
#     elif age >= 40 and age < 60:
#         return "assets/age/oldAdult.png"
#     else:
#         return "assets/age/elder.png"
