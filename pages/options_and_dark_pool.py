import streamlit as st
from utils.polygon_api import fetch_trades

def show():
    st.title("Options Flow and Dark Pool Data")

    ticker = st.text_input("Enter Ticker", value="AAPL")
    if ticker:
        # Fetch trades for the ticker
        trades_data = fetch_trades(ticker)

        # Filter for dark pool trades
        dark_pool_trades = [trade for trade in trades_data if trade['exchange'] == 4 and 'trf_id' in trade]

        st.subheader("Dark Pool Trades")
        st.write(dark_pool_trades)
