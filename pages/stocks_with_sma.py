import streamlit as st
from utils.stock_data import fetch_stock_data_with_sma

def show():
    st.title("Stocks with SMA Lines")
    
    ticker = st.text_input("Enter a stock ticker", value="AAPL")
    sma_short = st.slider("Short SMA Period", 0, 200, 50)
    sma_long = st.slider("Long SMA Period", 0, 200, 100)
    
    # Fetch stock data and calculate SMAs
    data = fetch_stock_data_with_sma(ticker, sma_short, sma_long)
    
    st.line_chart(data[['Close', f'SMA_{sma_short}', f'SMA_{sma_long}']])
