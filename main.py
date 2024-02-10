import streamlit as st
from polygon import RESTClient
import pandas as pd
import plotly.express as px

# Your Polygon API key
api_key = "wdt08q8wl_s8yxIO0TCQatAiMFnDxbvk"

# Initialize the Polygon client
client = RESTClient(api_key)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Options and Dark Pool", "Stocks with SMA"])

    if page == "Options and Dark Pool":
        show_options_and_dark_pool()
    elif page == "Stocks with SMA":
        show_stocks_with_sma()

def show_options_and_dark_pool():
    st.title("Options Flow and Dark Pool Data")

    # This is a placeholder for fetching and displaying options flow and dark pool data
    # You'll need to replace this with actual API calls to Polygon.io and data processing
    st.write("Options flow and dark pool data visualization goes here.")

def show_stocks_with_sma():
    st.title("Stocks with SMA Lines")

    ticker = st.text_input("Enter a stock ticker", value="AAPL")
    sma_short = st.slider("Short SMA Period", 0, 200, 50)
    sma_long = st.slider("Long SMA Period", 0, 200, 100)

    # Fetch stock data using your existing method or adjust to use Polygon if needed
    # For now, this uses a placeholder DataFrame
    dates = pd.date_range("2023-01-01", periods=100)
    data = pd.DataFrame({"Date": dates, "Close": (pd.Series(range(100)) + pd.Series(range(100)).apply(lambda x: x * 0.1))})
    data.set_index("Date", inplace=True)
    
    # Calculate SMAs
    data[f"SMA_{sma_short}"] = data["Close"].rolling(window=sma_short).mean()
    data[f"SMA_{sma_long}"] = data["Close"].rolling(window=sma_long).mean()

    # Plotting
    fig = px.line(data, y=["Close", f"SMA_{sma_short}", f"SMA_{sma_long}"], title=f"{ticker} Stock Price and SMAs")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
