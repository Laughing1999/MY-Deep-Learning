from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='my-input', value='Initial value', type='text'),
    html.Button('Click me', id='my-button'),
    html.Div(id='my-output')
])

@app.callback(
    Output('my-output', 'children'),
    Input('my-button', 'n_clicks'),
    State('my-input', 'value')
)
def update_output(n_clicks, input_value):
    return f'The button has been clicked {n_clicks} times, and the input value is "{input_value}".'

if __name__ == '__main__':
    app.run_server(debug=True)
