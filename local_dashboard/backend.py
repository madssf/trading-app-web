import requests
import config
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def get_token():
    creds = {'username': config.API_USER, 'password': config.API_PASS}
    data = requests.post(config.TOKEN_URL, data=creds)
    return data.json()['auth_token']


def get_portfolios(token):
    data = requests.get(config.GET_URL, headers={
                        'Authorization': f'Token {token}'})
    return data.json()


def get_market_data():
    return [{'symbol': coin['symbol'], 'price': coin['current_price'], 'mcap': coin['market_cap'], 'mcap_rank': coin['market_cap_rank']} for coin in cg.get_coins_markets(config.BASE_FIAT) if coin['symbol'].upper() not in config.STABLECOINS]
