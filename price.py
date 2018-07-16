import requests


def get_current_price():
    """
    Fetches BTC currency in USD from coinmarketcap.com.
    Returns currency and status(success==True or fail==False).
    """
    try:
        coin_api_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
        response = requests.get(coin_api_url)
        response_json = response.json()
        result = response_json[0]['price_usd'], True
    except:
        result = '', False

    return result
