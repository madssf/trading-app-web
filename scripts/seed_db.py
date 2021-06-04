from config import Superuser, Endpoints, Parameters
from backend.django_api import Api
from backend.coingecko import CoinGecko
import re
api_credentials = {'username': Superuser.USER2,
                   'password': Superuser.PW2}


api = Api(api_credentials, Endpoints.BASE, Endpoints.LOGIN)


cg = CoinGecko(Parameters.BASE_FIAT, Parameters.STABLECOINS)
market = cg.get_market_data(max=5)
for coin in market:
    name = "".join(re.findall("[a-zA-Z]+", coin['name']))
    symbol = "".join(re.findall("[a-zA-Z]+", coin['symbol']))
    slug = symbol
    data = {'slug': slug, 'name': coin['name'], 'symbol': coin['symbol'], 'last_price': coin['price'],
            'mcap_total': coin['mcap'], 'mcap_rank': coin['mcap_rank'], 'pct_change_24h': coin['pct_change_24h']}
    # Check if coin is in DB and update it/creates a new instance.

    post_res = api.make_request("POST", "currencies/", data=data)

    for item in post_res:
       # print(str(res[item]))
        if 'already exists' in str(post_res[item]):
            patch_res = api.make_request(
                "PATCH", f"currencies/symbol/{slug}/edit/", data=data)
            break
