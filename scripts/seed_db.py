from config import Superuser, Endpoints, Parameters
from backend.django_api import Api
from backend.coingecko import CoinGecko

api_credentials = {'username': Superuser.USER2,
                   'password': Superuser.PW2}


api = Api(api_credentials, Endpoints.BASE, Endpoints.LOGIN)


cg = CoinGecko(Parameters.BASE_FIAT, Parameters.STABLECOINS)
market = cg.get_market_data()
i = 0
for coin in market:
    currencies_data = {'name': coin['name'], 'symbol': coin['symbol'], 'last_price': coin['price'],
                       'mcap_total': coin['mcap'], 'mcap_rank': coin['mcap_rank'], 'pct_change_24h': coin['pct_change_24h']}
    res = api.make_request("POST", "currencies/", currencies_data)
    print(res)
