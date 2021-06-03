from os import pardir
from config import Superuser, Endpoints, Parameters
from backend.django_api import Api
from backend.coingecko import CoinGecko

api_credentials = {'username': Superuser.USER2,
                   'password': Superuser.PW2}


api = Api(api_credentials, Endpoints.BASE, Endpoints.LOGIN)

pfs = api.make_request("GET", "portfolios")
print(pfs)
cg = CoinGecko(Parameters.BASE_FIAT, Parameters.STABLECOINS)
market = cg.get_market_data()
for coin in market:
    api.make_request("POST", "currencies", coin)
