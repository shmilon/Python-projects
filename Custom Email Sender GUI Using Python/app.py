import os
import smtplib as smtp
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, callback, dash_table, dcc, html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################################################

sitelogo = "https://www.pngmart.com/files/15/Email-Symbol-PNG-Transparent-Picture.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=sitelogo, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Custom Mail Server", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)
########################################################################

#submit input field design using bootstrap
custom_form = dbc.Row([

    dbc.Label("Enter Receiver's Email:",
              html_for="custom_form", width=10),
    dbc.Col(dbc.Input(type="email",
                      min=1, step=100,
                      id="email",
                      placeholder="Receiver Email", required=1),
                width=100,
            ),
    dbc.FormFeedback("That looks like a integer value :-)", type="valid"),
    dbc.FormFeedback(
        "Sorry, we only accept integer ...", type="invalid",
    ),


    dbc.Label("Subject:",
              html_for="sub", width=10),
    dbc.Col(dbc.Input(type="text",
                      min=1, step=1,
                      id="sub",
                      placeholder="Subject", required=1),
                width=10,
            ),
    dbc.FormFeedback("That looks like a integer value :-)", type="valid"),
    dbc.FormFeedback("Sorry, we only accept integer ...", type="invalid",),

    dbc.Label("Message", 
              html_for="message", 
              width=10),
    dbc.Col(dbc.Textarea(className="mb-4", 
                         id="message",
                         placeholder="A Textarea"),
                         width=10,
                         ),
    dbc.FormFeedback("That looks like a integer value :-)", type="valid"),
    dbc.FormFeedback("Sorry, we only accept integer ...", type="invalid",),

], 

)

# submit form design
def Input_form():
    markdown = ''' '''
    form = html.Div([dbc.Container([
        dcc.Markdown(markdown), html.Br(), dbc.Card(
            dbc.CardBody([
                    dbc.Form([custom_form]), html.Div(id='div-button', children=[
                        dbc.Button('Send', color='primary',
                                   id='submit_form', n_clicks=0)
                    ])  # end div
                    ])  # end cardbody
        )  # end card
        , html.Br(), html.Br()
    ])
    ])
    return form

## toast design
toast = html.Div(
    [
        dbc.Toast(
            "",
            id="positioned-toast",
            header="Notification",
            is_open=False,
            duration=6000,
            icon="primary",
            # top: 66 positions the toast below the navbar
            style={"position": "fixed", "top": 66, "right": 10, "width": 350},
        ),
    ]
)
## end toast design


# html design executing using app.layout method
app.layout = html.Div([
    navbar,html.Br(), 
    html.H1(children='Custom Email Sender Tool',
            style={
                'textAlign': 'center',
                'color': 'blue'
            }
            ),
    html.H1(id="resultShow",
            style={
                'textAlign': 'center',
                'color': 'red'
            }
            ), Input_form(), html.Br(),toast,
])

@app.callback(
   # Output("alert-auto", "children"),
    #Output("alert-auto", "is_open"),

    Output("positioned-toast", "children"),
    Output("positioned-toast", "is_open"),
    [Input("submit_form", "n_clicks")],
    [State("email", "value"),
     State("sub", "value"),
     State("message", "value")],
)

# after value receive predicting the result
def update_output(n_clicks, receiver, sub,message):
    if n_clicks >0:
        if receiver !="" and sub != "" and message != "":

            # importing main prediction tool
            import controller
            res = controller.sendMail(receiver,sub,message)
            return f"Email {res} to {receiver}", True
        else:
            return "Invalid input", True
    return "", False  # No alert message when the page loads or on initial click

# run app
if __name__ == "__main__":
    app.run_server(debug=False)
