import pathlib
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State, callback  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("atussum_0321-reduced.csv"))


customize_layout = html.Div(
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
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Time 1"),
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
                                        html.Label("Time 2"),
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
                                        html.Label("Time 3"),
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
                                        html.Label("Time 4"),
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
                                        html.Label("Time 5"),
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
                                        html.Label("Time 6"),
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
                dbc.Col(
                    [
                        html.Button(
                            id="hit-button",
                            children="Submit",
                            className="btn btn-outline-primary",
                            # style={"float": "right"},
                        )
                    ],
                    width=12,
                )
            ],
            className="mt-4",
        ),
        # dbc.Row(
        #     [
        #         dbc.Col([dcc.Graph(id="myscatter", figure={})], width=6),
        #         dbc.Col([dcc.Graph(id="myscatter2", figure={})], width=6),
        #     ]
        # ),
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [
        #                 html.P(
        #                     id="notification",
        #                     children="",
        #                     style={"textAlign": "center"},
        #                 )
        #             ],
        #             width=12,
        #         )
        #     ]
        # ),
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
        return True
    else :
        return False

# # pull data from twitter and create the figures
# @app.callback(
#     Output(component_id="myscatter", component_property="figure"),
#     Output(component_id="myscatter2", component_property="figure"),
#     Output(component_id="notification", component_property="children"),
#     Input(component_id="hit-button", component_property="n_clicks"),
#     State(component_id="count-mentions", component_property="value"),
#     State(component_id="input-handle", component_property="value"),
# )
# def display_value(nclicks, num, acnt_handle):
#     results = api.GetSearch(
#         raw_query=f"q=%40{acnt_handle}&src=typed_query&count={num}"
#     )       #       q=%40MoveTheWorld%20until%3A2021-08-05%20since%3A2021-01-01&src=typed_query

#     twt_followers, twt_likes, twt_count, twt_friends, twt_name = [], [], [], [], []
#     for line in results:
#         twt_likes.append(line.user.favourites_count)
#         twt_followers.append(line.user.followers_count)
#         twt_count.append(line.user.statuses_count)
#         twt_friends.append(line.user.friends_count)
#         twt_name.append(line.user.screen_name)

#         print(line)

#     d = {
#         "followers": twt_followers,
#         "likes": twt_likes,
#         "tweets": twt_count,
#         "friends": twt_friends,
#         "name": twt_name,
#     }
#     df = pd.DataFrame(d)
#     print(df.head())

#     most_followers = df.followers.max()
#     most_folwrs_account_name = df["name"][df.followers == most_followers].values[0]

#     scatter_fig = px.scatter(
#         df, x="followers", y="likes", trendline="ols", hover_data={"name": True}
#     )
#     scatter_fig2 = px.scatter(
#         df, x="friends", y="likes", trendline="ols", hover_data={"name": True}
#     )
#     message = f"The Twitter account that mentioned @{acnt_handle} from Jan-Aug of 2021 is called {most_folwrs_account_name} and it has the highest followers count: {most_followers} followers."

#     return scatter_fig, scatter_fig2, message