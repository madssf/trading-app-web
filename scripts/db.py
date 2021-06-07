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

        # check if db has currencies that we haven't included
        # add those to market

        market = json.dumps(market)
        self.api.make_request(
            "POST", "bot/currencies", data=market)

    def get_credentials(self):
        return self.api.make_request("GET", "bot/credentials")

    def get_exchange_assets(self):

        creds = self.get_credentials()
        portfolios = {}

        for cred in creds:
            if not cred['portfolio_id'] in portfolios.keys():
                portfolios[cred['portfolio_id']] = []
            raw_assets = self.get_assets(
                exchange=cred['exchange'], key=cred['key'], secret=cred['secret'])

            # Cleaning assets
            cleaned_assets = []
            if cred['exchange'].lower() == 'binance':
                for symbol in raw_assets.items():
                    if isinstance(symbol[1], dict):
                        try:
                            amount = symbol[1]['total']
                            symbol = symbol[0]

                            if amount > 0:
                                status = "SPOT"

                                # set status to something else if needed
                                if symbol[:2] == "LD":
                                    status = "FLEX"
                                    symbol = symbol[2:]
                                if symbol == "BETH":
                                    status = "LOCK"
                                    symbol = "ETH"
                                cleaned_assets.append(
                                    {'symbol': symbol, 'status': status, 'amount': amount})
                        except (KeyError):
                            # loads of stuff in binance response
                            # ignoring everything that is not a dict
                            pass

            else:
                raise ValueError(f"Invalid exchange {cred['exchange']}")
            if len(cleaned_assets) > 0:
                portfolios[cred['portfolio_id']].append(
                    {'name': cred['exchange'], 'assets': cleaned_assets})

        assets = [{'portfolio': p, 'exchanges': portfolios[p]}
                  for p in portfolios]

        return assets

    def update_exchange_assets(self):
        data = self.get_exchange_assets()
        res = self.api.make_request(
            "POST", "bot/exchange_assets", data=json.dumps(data))
        return res

    def get_strategy_portfolios(self):
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
# db.update_currencies(n=250)
db.update_exchange_assets()
