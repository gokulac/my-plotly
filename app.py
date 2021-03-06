import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/gokulac/my-plotly/master/data.csv')

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.Button("Switch Axis", id='btn', n_clicks=1)
])

@app.callback(
    Output("graph", "figure"), 
    [Input("btn", "n_clicks")])
def display_graph(n_clicks):
    x, y = 'returns', 'date'

    # if n_clicks % 2 == 0:
    #     x, y = 'date', 'returns'
    # else:
    #     x, y = 'returns', 'date'



    fig = px.bar(df, x=x, y=y, orientation='h')    
    return fig

app.run_server(debug=True)