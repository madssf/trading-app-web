from backend.django_api import Api
from backend.coingecko import CoinGecko
import ccxt

from config import Superuser, Endpoints, Parameters

import re
import json


class DBConnection():

    def __init__(self):
        self.api = Api(
            {'username': Superuser.USERS[1], 'password': Superuser.PASSWORDS[1]}, Endpoints.BASE, Endpoints.LOGIN)
        self.cg = CoinGecko(Parameters.BASE_FIAT, Parameters.STABLECOINS)

    def update_currencies(self, n=5):
        market = self.cg.get_market_data(max=min(n, 250))  # coingecko 250 max
        print(f"Market size: {len(market)}")
        i = 0
        for coin in market:
            name = "".join(re.findall("[a-zA-Z.]+", coin['name']))
            symbol = "".join(re.findall("[a-zA-Z]+", coin['symbol']))
            market[i]['name'] = name
            market[i]['symbol'] = symbol
            market[i]['last_price'] = coin['price']
            del market[i]['price']
            i += 1
        market = json.dumps(market)
        self.api.make_request(
            "POST", "bot/currencies", data=market)

    def get_credentials(self):
        return self.api.make_request("GET", "bot/credentials")

    def get_exchange_assets(self):

        creds = self.get_credentials()
        assets = {}

        for cred in creds:
            if not cred['portfolio_id'] in assets.keys():
                assets[cred['portfolio_id']] = []
            raw_assets = self.get_assets(
                exchange=cred['exchange'], key=cred['key'], secret=cred['secret'])

            # Cleaning assets
            cleaned_assets = []
            if cred['exchange'].lower() == 'binance':
                for symbol in raw_assets.items():
                    if isinstance(symbol[1], dict):
                        try:
                            if symbol[1]['total'] > 0:
                                cleaned_assets.append(
                                    {symbol[0]: symbol[1]['total']})
                        except (KeyError):
                            # loads of stuff in binance response
                            pass

            else:
                raise ValueError(f"Invalid exchange {cred['exchange']}")
            if len(cleaned_assets) > 0:
                assets[cred['portfolio_id']].append(
                    {'exchange': cred['exchange'], 'assets': cleaned_assets})

        return assets

    def get_tradeable_portfolios(self):
        pass

    def post_trades(self):
        pass

    def get_assets(self, exchange, key, secret):
        exchange_class = getattr(ccxt, exchange.lower())
        exchange = exchange_class({
            'apiKey': key,
            'secret': secret,
        })
        return exchange.fetch_balance()


db = DBConnection()


data = db.get_exchange_assets()
print(data)
