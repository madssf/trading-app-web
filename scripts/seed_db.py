import json
from config import Superuser, Endpoints, Parameters
from backend.django_api import Api
from backend.coingecko import CoinGecko
import re
api_credentials = {'username': Superuser.USER2,
                   'password': Superuser.PW2}


class Seed():

    def __init__(self):
        self.api = Api(api_credentials, Endpoints.BASE, Endpoints.LOGIN)
        self.cg = CoinGecko(Parameters.BASE_FIAT, Parameters.STABLECOINS)

    def update_currencies(self, n=5):
        market = self.cg.get_market_data(max=n)
        i = 0
        for coin in market:
            name = "".join(re.findall("[a-zA-Z]+", coin['name']))
            symbol = "".join(re.findall("[a-zA-Z]+", coin['symbol']))
            market[i]['name'] = name
            market[i]['symbol'] = symbol
            i += 1
        market = json.dumps(market)
        print(market)
        res = self.api.make_request(
            "POST", "bot/currency_batch_update", data=market)
        print(res)


s = Seed()
s.update_currencies(n=10)
