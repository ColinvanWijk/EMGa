import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def mesag_size():
    # ---------- FILE HAS WRONG SIZE ----------- #
    A = dcc.ConfirmDialog(
        id='table_size',
        message='Bid file extension must be .cvs or .xls. ' +
        'Table must contain 24 rows and 2 columns',

    )
    ##############################################
    return  A


def mesag_nom():
    # ---------- BID > THAN NOMINAL P ----------- #
    B = dcc.ConfirmDialog(
        id='compare_p',
        message='CAUTION!  There are Bid values greater than Nominal Power.',
    )
    ##############################################
    return B


def mesag_confirm_trade():
    # ---------- BID > THAN NOMINAL P ----------- #
    BB = html.Div([

        dbc.Modal(
            [
                dbc.ModalHeader("Confirm Transaction"),
                dbc.ModalBody([
                    html.P(
                        dcc.Markdown(
                            "Are you sure you want to submit your bid?"
                        )
                    ),
                ]
                ),
                dbc.ModalFooter([
                    html.Div([
                        dcc.Link(html.Button("OK Trade!", id="ok_button", className='button-primary', ),
                                 id='link_conf_trade', href='/Page_2'),
                    ], style={'textAlign': 'left'}),

                    html.Div([
                        dcc.Link(html.Button("Cancel", id="cancel_button", className='button-primary', ),
                                 id='link_conf_trade', href='/Page_1')
                    ], style={'textAlign': 'right'})



                ],style={'textAlign': 'center'}
                ),
            ], id="modal_conf_trade", backdrop="static", scrollable=True, centered=True, style={'textAlign': 'center'}
        ),

    ])

    #     dcc.ConfirmDialog(
    #     id='confirm_trade',
    #     message='CAUTION!  Are you sure you are ready to submit your trade?',
    # )
    ##############################################
    return BB


