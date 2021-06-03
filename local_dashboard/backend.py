import requests
import config
from pycoingecko import CoinGeckoAPI
from json import JSONDecodeError
cg = CoinGeckoAPI()


def get_token():
    creds = {'username': config.API_USER, 'password': config.API_PASS}
    data = requests.post(config.TOKEN_URL, data=creds)
    return data.json()['auth_token']


def get_portfolios(token):
    data = requests.get(config.GET_URL, headers={
                        'Authorization': f'Token {token}'})
    return data.json()


def get_req(token, endpoint):

    data = requests.get(config.API_URL+endpoint, headers={
                        'Authorization': f'Token {token}'})
    try:
        return data.json()
    except JSONDecodeError:
        return data.text


def get_market_data():
    return [{'symbol': coin['symbol'], 'price': coin['current_price'], 'mcap': coin['market_cap'], 'mcap_rank': coin['market_cap_rank']} for coin in cg.get_coins_markets(config.BASE_FIAT) if coin['symbol'].upper() not in config.STABLECOINS]
