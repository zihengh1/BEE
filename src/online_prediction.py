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
                        html.Div([
                            html.P("Total time:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                            html.Span(id="total_time", style={'font':'Monospace','color':'#66B3FF', 'font-size':'1.5em', 'text-decoration':'underline', 'display': 'inline-block', "margin-left": "15px"}),
                        ])
                        
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

        dbc.Row(
            [
                 html.P("Your ID card", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2.5em', 'text-align':'center'})
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(id='age',style={"display":"block", "margin-left":"auto", "margin-right":"auto"}),
                                html.Br(),
                                html.P("Brian", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'text-align':'center'})
                            ],
                            style={'vertical-align':'middle'},
                        )
                    ],
                    width=4, 
                    style={'display':'flex', 'justify-content':'center', 'align-items': 'center', 'flex-flow': 'column'},
                ),
                dbc.Col(
                    [

                    ],
                    width=1,
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                html.Div([
                                    html.P("Age:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="ageRange", style={'font':'Monospace', 'font-size':'1.5em', 'text-decoration':'underline', 'display': 'inline-block', "margin-left": "15px"}),
                                ])
                            ]
                        ),
                        dbc.Row(
                            [
                                html.Div([
                                    html.P("Children:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Img(id="childNum", style={'max-height':'80px','object-fit': 'cover','display': 'inline-block', "margin-left": "15px"}),
                                    html.P(id='childRange', style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'0.9em', 'margin-top':'-10px'}),
                                ])
                            ]
                        ),
                        dbc.Row(
                            [
                                html.Div([
                                    html.P("Children's age:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="childAge", style={'font':'Monospace', 'font-size':'1.5em', 'text-decoration':'underline', 'display': 'inline-block', "margin-left": "15px"}),
                                ])
                            ]
                        ),
                        dbc.Row(
                            [
                                html.Div([
                                    html.P("Work Hours:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Img(id="workHours", style={'max-height':'100px','display': 'inline-block', "margin-left": "15px", 'object-fit': 'cover'}),
                                    html.P(id='workHoursRange', style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'0.9em', 'margin-top':'-10px'}),
                                ])
                            ]
                        ),
                    ],
                    width=7,
                ),
            ],
            style={"border":"5px solid", "border-radius" : "25px", "padding":'30px', "margin-left":"150px", "margin-right":"150px"}, className='mb-4'
        ),
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
    Output("ageRange", component_property="children"),
    Input("age_pred", component_property="data"),
)
def generate_age_figure(age):
    print(age)
    if age > 0 and age < 10 or age == 0:
        return "assets/age/baby.png", "0 - 10"
    elif age >= 10 and age < 20:
        return "assets/age/teenager.png", "10 - 20"
    elif age >= 20 and age < 40:
        return "assets/age/adult.png", "20 - 40"
    elif age >= 40 and age < 60:
        return "assets/age/oldAdult.png", "40 - 60"
    else:
        return "assets/age/elder.png", "60+"

@callback(
    Output("childNum", component_property="src"),
    Output("childRange", component_property="children"),
    Input("childNum_pred", component_property="data"),
)
def generate_childNum_figure(ch):
    childNum = math.ceil(ch)
    if childNum == 0 or childNum == 1:
        return "assets/childNum/infant_1.png", "(0 - 1)"
    else:
        return "assets/childNum/infant_2.png", "(2+)"
@callback(
    Output("childAge", component_property="children"),
    Input("childAge_pred", component_property="data"),
)
def generate_childAge(ca):
    childAge = ca
    if childAge > 0 and childAge < 5 or childAge == 0:
        return "0 - 5"
    elif childAge >= 5 and childAge < 10:
        return "5 - 10"
    elif childAge >= 10 and childAge < 15:
        return "10 - 15"
    else:
        return "15+"
@callback(
    Output("workHours", component_property="src"),
    Output("workHoursRange", component_property="children"),
    Input("workHours_pred", component_property="data"),
)
def generate_age_figure(wh):
    workHours = math.ceil(wh)
    if workHours > 0 and workHours <= 10 or workHours == 0:
        return "assets/workHours/wrench_1.png", "(0 - 10)"
    elif workHours > 10 and workHours <= 20:
        return "assets/workHours/wrench_2.png", "(10 - 20)"
    elif workHours > 20 and workHours <= 30:
        return "assets/workHours/wrench_3.png", "(20 - 30)"
    elif workHours > 30 and workHours <= 40:
        return "assets/workHours/wrench_4.png", "(30 - 40)"
    elif workHours > 40 and workHours <= 50:
        return "assets/workHours/wrench_5.png", "(40 - 50)"
    elif workHours > 50 and workHours <= 60:
        return "assets/workHours/wrench_6.png", "(50 - 60)"
    elif workHours > 60 and workHours <= 70:
        return "assets/workHours/wrench_7.png", "(60 - 70)"
    elif workHours > 70 and workHours <= 80:
        return "assets/workHours/wrench_8.png", "(70 - 80)"
    elif workHours > 80 and workHours <= 90:
        return "assets/workHours/wrench_9.png", "(80 - 90)"
    else:
        return "assets/workHours/wrench_10.png", "(90 - 100)"
    
