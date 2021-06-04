from pycoingecko import CoinGeckoAPI


class CoinGecko():

    def __init__(self, base_fiat, stablecoins):
        self.base_fiat = base_fiat
        self.stablecoins = stablecoins
        self.cg = CoinGeckoAPI()

    def get_market_data(self):
        return [{'name': coin['name'], 'symbol': coin['symbol'].upper(), 'price': coin['current_price'], 'mcap': coin['market_cap'], 'mcap_rank': coin['market_cap_rank'], 'pct_change_24h': coin['price_change_percentage_24h']} for coin in self.cg.get_coins_markets(self.base_fiat, per_page=250) if coin['symbol'].upper() not in self.stablecoins]
