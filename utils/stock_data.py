import pandas as pd
import requests

API_KEY = "wdt08q8wl_s8yxIO0TCQatAiMFnDxbvk"

def fetch_stock_data_with_sma(ticker, sma_short, sma_long, start_date, end_date):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/5/minute/{start_date}/{end_date}"
    params = {
        "apiKey": API_KEY,
        "adjusted": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return pd.DataFrame(), "Failed to fetch data"
    
    data = pd.DataFrame(response.json()['results'])
    if data.empty:
        return pd.DataFrame(), "No data available for the given range"
    
    # Convert timestamps to readable dates
    data['t'] = pd.to_datetime(data['t'], unit='ms')
    data.rename(columns={'t': 'Date', 'c': 'Close'}, inplace=True)
    data.set_index('Date', inplace=True)
    
    # Calculate SMAs
    data[f'SMA_{sma_short}'] = data['Close'].rolling(window=sma_short).mean()
    data[f'SMA_{sma_long}'] = data['Close'].rolling(window=sma_long).mean()

    return data, ""
