import streamlit as st
from utils.stock_data import fetch_stock_data_with_sma
import plotly.graph_objs as go

def show():
    st.title("Stocks with SMA Lines")
    
    ticker = st.text_input("Enter a stock ticker", value="AAPL")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    sma_short = st.slider("Short SMA Period", 0, 200, 50)
    sma_long = st.slider("Long SMA Period", 0, 200, 100)

    data, error_message = fetch_stock_data_with_sma(ticker, sma_short, sma_long, start_date, end_date)
    
    if error_message:
        st.error(error_message)
    else:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close'))
        fig.add_trace(go.Scatter(x=data.index, y=data[f'SMA_{sma_short}'], mode='lines', name=f'SMA {sma_short}'))
        fig.add_trace(go.Scatter(x=data.index, y=data[f'SMA_{sma_long}'], mode='lines', name=f'SMA {sma_long}'))
        
        fig.update_layout(title=f'{ticker} Stock Price and SMAs', xaxis_title='Date', yaxis_title='Price')
        st.plotly_chart(fig)
