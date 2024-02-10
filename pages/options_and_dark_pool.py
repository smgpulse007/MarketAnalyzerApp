import streamlit as st
from utils.polygon_api import fetch_options_flow_data, fetch_dark_pool_data

def show():
    st.title("Options Flow and Dark Pool Data")
    
    # Example ticker
    ticker = st.text_input("Enter Ticker", value="AAPL")
    
    # Assuming these functions return DataFrame or similar structured data
    options_data = fetch_options_flow_data(ticker)
    dark_pool_data = fetch_dark_pool_data(ticker)
    
    st.write("Options Flow Data", options_data)
    st.write("Dark Pool Data", dark_pool_data)
