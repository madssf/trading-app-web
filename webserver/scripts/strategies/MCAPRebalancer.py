

class MCAPRebalancer():
    '''
    Parameters:
          denominator
          weighted
          wiggle
          min_trade_abs
          min_trade
          profit_level
          banned_tags
          banned
          handpicked_mcap
          hard_hp_amts
          hard_hp
          max_coins
          min_coins
    '''

    def __init__(self, parameters, assets):
        self.parameters = parameters
        self.assets = assets
        # getting total per curerncy
        self.fiat_total = sum(asset['value'] for asset in self.assets.values())
        # for asset in assets:

    def instruct(self, market):

        # 1. Create balanced portfolio

        # 1.1 Get fiat value of portfolio

        # 2. Calculate difference

        return self.fiat_total
