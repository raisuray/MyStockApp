import yfinance as yf 
from downloader import getData
from plotting import makeChart

from dash import Dash
from dash import dcc
from dash import html
from  dash import Input, Output


app = Dash(__name__)

f = open("stock-list.txt", "r")
temp = f.readlines()
#stock_list = ["BBCA.JK", "MDKA.JK", "INDF.JK", "BBRI.JK"]
stock_list = []

for i in temp:
    stock_list.append(i[0:7])

print(stock_list[0])

app.layout = html.Div([
    html.H1(className="app-header", children='My App for Checking Stock'),
    html.H2(className="app-header", children='Stock-List'),
    dcc.Dropdown(
        stock_list,
        stock_list[0],
        id='Stock-list'
    ),
    dcc.Graph(
        id='Stock-graph',
        figure=makeChart(getData(stock_list[0]), stock_list[0]), 
        style={'height': '80vh'})
])

@app.callback(
    Output('Stock-graph', 'figure'),
    Input('Stock-list', 'value')
)
def generateChart(stock_name):
    return makeChart(getData(stock_name), stock_name)

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
