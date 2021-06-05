import json
from config import Superuser, Endpoints, Parameters
from backend.django_api import Api
from backend.coingecko import CoinGecko
import re
api_credentials = {'username': Superuser.USERS[1],
                   'password': Superuser.PASSWORDS[1]}


class DBUpdater():

    def __init__(self):
        self.api = Api(api_credentials, Endpoints.BASE, Endpoints.LOGIN)
        self.cg = CoinGecko(Parameters.BASE_FIAT, Parameters.STABLECOINS)

    def update_currencies(self, n=5):
        market = self.cg.get_market_data(max=min(n, 250))  # coingecko 250 max
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
        print(f"Market size: {len(market)}")
        self.api.make_request(
            "POST", "bot/currencies", data=market)

    def update_portfolio_assets(self):

        # get all portfolios with credentials
        # all_assets = []
        # for portfolio in portfolios:
        #   portfolio_assets = []
        #   for creds in credentials:
        #       portfolio_assets.append(get_assets(creds.exchange, credentials))
        #   if len(portfolio_assets > 0):
        #       all_assets.append(portfolio_assets)
        pass


s = DBUpdater()
s.update_currencies(n=250)
