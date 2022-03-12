import plotly.graph_objects as go
from plotly.subplots import make_subplots

def makeChart(hist, name):
    hist['diff'] = hist['Close'] - hist['Open']
    hist.loc[hist['diff']>=0, 'color'] = 'green'
    hist.loc[hist['diff']<0, 'color'] = 'red'
    
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
    fig3.add_trace(go.Candlestick(x=hist.index,
                                open=hist['Open'],
                                high=hist['High'],
                                low=hist['Low'],
                                close=hist['Close'],
                                name='Price'))
    fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].rolling(window=10).mean(),marker_color='blue',name='20 Day MA'))
    fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].rolling(window=50).mean(),marker_color='green',name='50 Day MA'))

    fig3.update_yaxes(range=[0,700000],secondary_y=True)
    fig3.update_yaxes(visible=False, secondary_y=True)
    fig3.update_layout(xaxis_rangeslider_visible=False)  #hide range slider
    fig3.update_layout(title={'text':name, 'x':0.5})
    return fig3
