import config
from pycoingecko import CoinGeckoAPI
import requests


def get_token():
    creds = {'username': config.API_USER, 'password': config.API_PASS}
    data = requests.post(config.TOKEN_URL, data=creds)
    return data.json()['auth_token']


def post_currency(token, data):
    data = requests.post(config.POST_URL, headers={
        'Authorization': f'Token {token}'}, data=data)
    return data.json()

# , 'price': coin['current_price'], 'mcap': coin['market_cap'], 'mcap_rank': coin['market_cap_rank']


def get_market_data():
    return [{'name': coin['name'], 'symbol': coin['symbol'].upper()} for coin in cg.get_coins_markets(config.BASE_FIAT) if coin['symbol'].upper() not in config.STABLECOINS]


cg = CoinGeckoAPI()


data = []

token = get_token()
for coin in get_market_data():
    '''
  'added_at', 'added_by', 'name',
                    'symbol', 'alternative_name', 'web_url', 'whitepaper_url', 'description'
    '''
    data = post_currency(token, coin)
    print(data)
