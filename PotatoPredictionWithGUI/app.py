# librarier for pydash
from dash import Dash, Input, Output, State, html, dcc, dash_table,  callback
import plotly.express as px
import dash_bootstrap_components as dbc
import os


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


#submit input field design using bootstrap
weight_input = dbc.Row([

    dbc.Label("How much weight\'s price do you want to predict ?",
              html_for="weight_input", width=10),
    dbc.Col(dbc.Input(type="number",
                      min=1, step=1,
                      id="weight_input",
                      placeholder="Enter Weight", required=1),
                width=10,
            ),
    dbc.FormFeedback("That looks like a integer value :-)", type="valid"),
    dbc.FormFeedback(
        "Sorry, we only accept integer ...", type="invalid",
    ),
], className="mb-3"
)

# submit form design
def weight_Input_form():
    markdown = ''' '''
    form = html.Div([dbc.Container([
        dcc.Markdown(markdown), html.Br(), dbc.Card(
            dbc.CardBody([
                    dbc.Form([weight_input]), html.Div(id='div-button', children=[
                        dbc.Button('Submit', color='primary',
                                   id='weight-submit', n_clicks=0)
                    ])  # end div
                    ])  # end cardbody
        )  # end card
        , html.Br(), html.Br()
    ])
    ])
    return form

# html design executing using app.layout method
app.layout = html.Div([
    html.H1(children='Potato Price Prediction',
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
            ), weight_Input_form(), html.Br()
])


@app.callback(
    Output("resultShow", "children"),
    [Input("weight-submit", "n_clicks")],
    [State("weight_input", "value")]
)

# after value receive predicting the result
def update_output(n_clicks, value):
    if value != "":

        # importing main prediction tool
        import main
        res = main.normalize_predict(value)
        return "Price: {} KG = {} Tk ".format(value, res)


# run app
if __name__ == "__main__":
    app.run_server(debug=False)
