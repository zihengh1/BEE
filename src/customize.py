import pathlib
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("atussum_0321-reduced.csv"))

customize_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Time 1"),
                        html.Br(),
                        dcc.Input(
                            id="input-handle_1",
                            type="text",
                            placeholder="Insert time here",
                            value="100",
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        html.Label("Time 2"),
                        html.Br(),
                        dcc.Input(
                            id="input-handle_2",
                            type="text",
                            placeholder="Insert time here",
                            value="100",
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        html.Label("Time 3"),
                        html.Br(),
                        dcc.Input(
                            id="input-handle_3",
                            type="text",
                            placeholder="Insert time here",
                            value="100",
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        html.Label("Time 4"),
                        html.Br(),
                        dcc.Input(
                            id="input-handle_4",
                            type="text",
                            placeholder="Insert time here",
                            value="100",
                        ),
                    ],
                    width=3,
                ),
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
                            style={"float": "right"},
                        )
                    ],
                    width=11,
                )
            ],
            className="mt-4",
        ),
        dbc.Row(
            [
                dbc.Col([dcc.Graph(id="myscatter", figure={})], width=6),
                dbc.Col([dcc.Graph(id="myscatter2", figure={})], width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            id="notification",
                            children="",
                            style={"textAlign": "center"},
                        )
                    ],
                    width=12,
                )
            ]
        ),
    ]
)


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