import requests

# Your Polygon API key
API_KEY = "wdt08q8wl_s8yxIO0TCQatAiMFnDxbvk"

def fetch_aggregates(ticker, multiplier, timespan, from_date, to_date):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    params = {
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

def fetch_last_trade(ticker):
    url = f"https://api.polygon.io/v2/last/trade/{ticker}"
    params = {
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

def fetch_last_quote(ticker):
    url = f"https://api.polygon.io/v2/last/nbbo/{ticker}"
    params = {
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()
    
def fetch_trades(ticker):
    url = f"https://api.polygon.io/vX/trades/{ticker}"
    params = {
        "apiKey": API_KEY,
        # Additional parameters might be needed depending on the API's filtering capabilities
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        trades = response.json()
        return trades['results']  # Adjust based on the actual structure of the API response
    else:
        return []
