from .backend.django_api import Api
from .backend.coingecko import CoinGecko
import ccxt

from .config import Endpoints, Parameters

import re
import json


class DBConnection():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api = Api(
            {'username': self.username, 'password': self.password}, Endpoints.BASE, Endpoints.LOGIN)
        self.cg = CoinGecko(Parameters.BASE_FIAT)

    def update_currencies(self, per_page=250, pages=2):
        market = []
        for i in range(pages):
            # coingecko 250 max
            market += self.cg.get_market_data(i+1, max=min(per_page, 250))

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

        self.api.make_request(
            "POST", "bot/currencies", data=json.dumps(market))
        return market

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

    # returns all portfolios with strategies, credentials, parameters and assets
    def get_strategy_portfolios(self):
        res = self.api.make_request("GET", "bot/strategy_portfolios")
        return res

    def update_instructions(self, data):
        return self.api.make_request("POST", "bot/strategy_instructions", data=json.dumps(data))

    def get_assets(self, exchange, key, secret):
        exchange_class = getattr(ccxt, exchange.lower())
        exchange = exchange_class({
            'apiKey': key,
            'secret': secret,
        })
        return exchange.fetch_balance()



    def email_notify(self, portfolio):
        print(f"sending email to{portfolio['email']}")