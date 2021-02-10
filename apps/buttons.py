import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app
import dash_bootstrap_components as dbc


# BUTT = html.Div([
#     dbc.Button("Primary", color="primary", className="mr-1"),
# ]
# ),

def submit_b():
    A = html.Div([
        html.Div([
            # dcc.Link(html.Button('3. Submit', id='button', disabled=True, style={'color':app.color_4})),
            dcc.Link(
                html.Button('TRADE', id='button', type='submit',
                            style={'font-size': '1.2vw'}, className='disabled',disabled=True),
                # dbc.Button(size='md', color="success", outline=True, children='TRADE', id='button', disabled=True,
                #            style={'font-size': '1.2vw'}),
                href='/Page_2'),
            html.Div(id='Button_data',
                     children='',
                     # style={'color': app.color_8, 'font-size': '22px', 'textAlign': 'center'}
                     )
        ]),

        # dbc.Container(
        #     html.Div(
        #     BUTT,
        #     ),
        # ),

    ])
    return A


def next_day():
    B = html.Div([
        html.Div([
            dcc.Link(
                html.Button(className='button-primary', children='Go to Next Day\'s Bid', id='nextD_b',
                           disabled=False, style={
                        # 'marginTop':'165%',
                        'marginBottom': '5%', 'font-size': '0.7vw', }),
                id='link_b2', href='/Page_1'),
        ], style={'textAlign': 'center', 'width': '100%', 'height': '100%'}),

    ])
    return B


def download_data():
    C = html.Div([
        html.Div([

            html.A(
                dcc.Loading(id='loading_1', color=app.color_3, type='circle'),
                   id='link_downl',
                   download="",
                   href="",
                   target="_blank",
                   ),
        ]),  #

    dbc.Tooltip(
        "Historical 15-minute normalized power data.",
        target="link_downl", placement='right', style={'font-size': '0.7vw'}
    ),

    ])


    return C

def download_irrad():
    I = html.Div([
        html.Div([

            html.A(dcc.Loading(id='loading_3', color=app.color_3, type='circle'),
                   id='link_downl3',
                   download="",
                   href="",
                   target="_blank",
                   ),
        ]),  #

    ])
    return I

# def port_info():
#     G = html.Div([
#
#         html.A(dcc.Loading(id='loading_4', color=app.color_3, type='default'),
#                id='port_dwnl',
#                download="",
#                href="",
#                target="_blank"
#                ),
#         ])
#
#     return G


def download_DAP():
    D = html.Div([
        html.Div([

            html.A(dcc.Loading(id='loading_2', color=app.color_3, type='circle'),
                   id='link_downl_dap',
                   download="",
                   href="",
                   target="_blank"
                   ),
        ]),  #

    dbc.Tooltip(
        "Historical hourly day-ahead prices.",
        target="link_downl_dap", placement='right', style={'font-size': '0.7vw'}
    ),

    ])
    return D

def imb_factors():
    FF = html.Div([
        html.Div([

            html.A(dcc.Loading(id='loading_5', color=app.color_3, type='circle'),
                   id='link_downl_imb',
                   download="",
                   href="",
                   target="_blank"
                   ),
        ]),  #

    dbc.Tooltip(
        "Hourly imbalance factors (known data for current trading day).",
        target="link_downl_imb", placement='right', style={'font-size': '0.7vw'}
    ),

    ])
    return FF


def return_page1():
    E = html.Div([
        html.Div(dcc.LogoutButton(logout_url='/logout',
                                  className='button-logout',
                                  style={'font-size': '0.8vw',
                                         'vertical-align': 'middle',
                                         'height': '2vw'}, ),
                 style={'display': 'inline-block', 'height': '5vw'},
                 id='logout_but2', ),
        # html.Div([
        #     dcc.Link(
        #         dbc.Button(size='lg', color="success", outline=True, children='Return', id='return_b',
        #                    disabled=False, style={
        #                 # 'marginTop':'165%',
        #                 'marginBottom': '5%', 'font-size': '0.7vw', }),
        #         id='link_b2', href='/logout'),
        # ], style={'textAlign': 'center', 'width': '100%', 'height': '100%'}),

    ])
    return E


def help_drag():
    F = html.Div([

            html.Div([
                html.Button([

                    html.Div([
                        html.Div([html.H2('Help ',
                                          style={'font-size': '1.0vw', 'color': app.color_4, 'display': 'inline-block',
                                                 'text-transform': 'capitalize'}),
                                  html.Img(
                                      src='https://raw.githubusercontent.com/juan-giraldo-ch/Serious_Game/master/question.svg',
                                      style={'display': 'inline-block', 'height': '1.5vw', 'width': '1.5vw'},
                                      title='Help',
                                  ),
                                  ],
                                 style={'display': 'inline-block'}),

                    ],
                        style={'display': 'inline-block', 'height': '100%'}
                    ),

                ], id='your_button', style={'height': '3vw', 'border': 'none', 'background': 'none'}
                ),

    dbc.Tooltip(
        "Game guidelines",
        target="your_button", placement='right', style={'font-size': '0.7vw'}
    ),

            ], style={'display': 'inline-block', 'textAlign': 'center'}
            ),

        dbc.Modal(
            [
                dbc.ModalHeader("Guidelines"),
                dbc.ModalBody([
                    html.P(
                      dcc.Markdown(
                          "***Game Instructions***:"
                      )
                    ),

                    html.P(
                        dcc.Markdown(
                            "**1)** You can download the updated historical data for your wind farm,"
                            "  the day-ahead prices (updated for each trading day), and the imbalance factors."
                            " Also, you can check the operational limits of your portfolio."
                    # "Download past wind speed records by clicking on the `Download Historical Wind Data` "
                    #         " button. Also, get the day-ahead prices from the `Download Day Ahead Prices` button."
                        ),
                    ),
                    html.P(
                        dcc.Markdown(
                            "**2)** Use a forecasting technique to estimate the total hourly energy of your portfolio"
                            " for the next trading day. Use the forecasted values to obtain a **`bid file`** using a "
                            "decision making technique."
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            ">***Obs.*** You can download a template file in the ***`Toolbox`*** section."
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "**3)** Upload and submit your **`bid file`**, containing the expected hourly energy bids obtained"
                            " in step 2 separated by energy source. Your file must have extensions .csv or .xls"
                            " and should contain **`25`** rows and **`5`** columns in total."
                            " You can drag the file or select it from your computer. Check the uploaded data file in the table."
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "**4)** Click on the **`TRADE`** button to submit your energy bids and continue playing."
                        ),
                    ),

                    html.P(
                        dcc.Markdown(
                            "**5)** You will be redirected to the performance page, where you can review your day"
                            " performance by comparing your actual revenue and the maximum revenue (perfect forecast)."
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "**6)** After checking your revenue, you can continue to the next trading day "
                            "by clicking on the button **`Go to Next Day's Bid`**."
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "**7)** Once you click on the **`Go to Next Day's Bid`** button, you will be redirected back to"
                            " the main page. To continue with the game, repeat this guide from step 2. "
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "**8)** The game finishes when there are no more available trading days. You will be"
                            " immediately redirected to the summary page where you can see your final stats. When all"
                            " players have finished the game, the **WINNER** will be the player that appears in the"
                            " first position of the **`Leaderboard`**."
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "---"
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "***Leaderboard***:"
                        )
                    ),

                    html.P(
                        dcc.Markdown(
                            "**1)** You can check the **leaderboard** by clicking on the **`LEADERBOARD`** button."
                        )
                    ),

                  html.P(
                      dcc.Markdown(
                          "**2)** The **leaderboard** displays your accumulated revenue, "
                          " the number of days you have played, and your **`Rate`**."
                      )
                  ),

                html.P(
                    dcc.Markdown(
                        "**3)** The **`Rate`** is the ratio between your **`Accumulated Revenue`**/**`Played days`**. "
                        " The **`Rate`** is the measurement for the game's ranking... "
                        "**So keep it as high as possible!!**"
                    )
                )


            ]

                ),
                dbc.ModalFooter(
                    html.Button("Let's Play!", id="close", className='button-primary',)
                ),
            ], id="modal", backdrop="static", scrollable=True, centered=True,
        ),

    ], style={'display': 'inline-block'})

    return F


