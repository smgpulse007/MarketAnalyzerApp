import pandas as pd
from polygon import RESTClient

def fetch_stock_data_with_sma(ticker, sma_short, sma_long):
    with RESTClient("your_polygon_api_key") as client:
        # Fetch stock data
        # Implement based on your data needs, this is a placeholder
        stock_data = pd.DataFrame()  # Placeholder for actual API call
        
        # Calculate SMAs
        stock_data[f'SMA_{sma_short}'] = stock_data['Close'].rolling(window=sma_short).mean()
        stock_data[f'SMA_{sma_long}'] = stock_data['Close'].rolling(window=sma_long).mean()
        
        return stock_data
