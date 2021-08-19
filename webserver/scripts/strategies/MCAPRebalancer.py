import ast
import math

class MCAPRebalancer():
    '''
    Parameters:
          denominator - string
          weighted - float
          wiggle - float
          min_trade_abs - float
          min_trade - float
          profit_level - float
          max_coins - int
          min_coins - int
          banned_tags - list[string] <-- ignore, added to banned by backend
          banned - list[string]
          soft_hp - list[string]
          hard_hp - list[tuple]
    '''

    def __init__(self, parameters, assets):
        self.parameters = self.parse_parameters(parameters)
        self.assets = assets
        # getting total per curenncy
        self.balanced_portfolio = None
        self.diffs = None
        self.fiat_total = None
        # for asset in assets:

    def instruct(self, market):
        balanced_portfolio = self.generate_balanced_portfolio(market)
        diff_matrix = self.generate_diff_matrix(balanced_portfolio, market)
        gains = self.calculate_gains()
        if self.check_trade_conditions(balanced_portfolio, diff_matrix, gains):
            return self.generate_instructions(balanced_portfolio, diff_matrix, gains)
        else:
            return False

    def check_trade_conditions(self, balanced_portfolio, diff_matrix, gains):

        # 1. Free fiat to trade for?
        if self.assets.get(self.parameters['denominator'], {}).get('value', 0) > self.parameters['min_trade_abs']:
            return True

        # 2. Take profit?
        for symbol in gains:
            if gains[symbol] > self.parameters['profit_level'] and diff_matrix[symbol]['fiat'] > self.parameters['min_trade']:
                return True

        # 3. Dropped coins?
        for symbol in self.assets:
            if symbol not in balanced_portfolio.keys() and diff_matrix[symbol]['fiat'] >= self.parameters['min_trade_abs']:
                return True
            
        return False
    
    def calculate_gains(self):
        return {symbol: (
            float(self.assets[symbol]['last_price']) - float(self.assets[symbol]['average'])) / float(self.assets[symbol]['average']) if self.assets[symbol]['average'] != None else 0 
            for symbol in self.assets}

    def generate_instructions(self, balanced_portfolio, diff_matrix, gains):
        
        instructions = []
        new_coins = []
        if self.assets.get(self.parameters['denominator'], False):
            free_fiat = self.assets[self.parameters['denominator']]['value']
        else:
            free_fiat = 0

        for symbol in diff_matrix:

            if symbol == self.parameters['denominator']:
                continue
            if symbol not in self.assets.keys():
                new_coins.append(symbol)
                continue
            liquid = self.assets[symbol]['value'] - sum(x['value'] for x in self.assets[symbol]['positions'] if x['status'] == "LOCK")
            if liquid < self.parameters['min_trade_abs']:
                continue

            # SELLING: Dropped coins or take profit
            if (symbol not in balanced_portfolio.keys() and diff_matrix[symbol]['fiat'] >= self.parameters['min_trade_abs']) or (gains[symbol] > self.parameters['profit_level'] and diff_matrix[symbol]['fiat'] > self.parameters['min_trade']):
                instructions.append({
                    'symbol': symbol,
                    'fiat' : diff_matrix[symbol]['fiat'], 
                    'tokens': diff_matrix[symbol]['tokens'], 
                    'side': "SELL"})
                free_fiat += diff_matrix[symbol]['fiat']

        # Check fiat amount before doing buys
        if free_fiat < self.parameters['min_trade_abs']:
            return False
        
    
        # BUYING
        # Prio 1: Hard handpicks
        for symbol in self.parameters['hard_hp']:
            diff = -diff_matrix[symbol]['fiat']
            if diff > self.parameters['min_trade_abs'] and diff < free_fiat:
                instructions.append({
                    'symbol': symbol,
                    'fiat' : -diff_matrix[symbol]['fiat'], 
                    'tokens': -diff_matrix[symbol]['tokens'], 
                    'side': "BUY"})
                free_fiat -= diff
                del diff_matrix[symbol]
            elif diff > free_fiat:
                instructions.append({
                    'symbol': symbol,
                    'fiat' : free_fiat, 
                    'tokens': free_fiat/diff_matrix[symbol]['price'], 
                    'side': "BUY"})
                return instructions
        
        # Prio 2: Sort by missing amount, split as many as possible
        sorted_missing = sorted({symbol: diff_matrix[symbol]['fiat'] for symbol in diff_matrix if symbol not in self.parameters['hard_hp'] and diff_matrix[symbol]['fiat'] < 0}.items(), key=lambda x: x[1])
        mcap_coins = {}
        for element in sorted_missing:
            symbol = element[0]
            missing = mcap_coins.get(symbol, 0) - diff_matrix[symbol]['fiat']
           
            if missing < free_fiat:
                mcap_coins[symbol] = mcap_coins.get(symbol, 0 ) + missing
                free_fiat -= missing
            else:
                mcap_coins[symbol] = mcap_coins.get(symbol, 0 ) + free_fiat
                free_fiat = 0
                break
         
        for symbol in mcap_coins:
            instructions.append({
                    'symbol': symbol,
                    'fiat' : mcap_coins[symbol], 
                    'tokens': mcap_coins[symbol]/diff_matrix[symbol]['price'], 
                    'side': "BUY"})
        
        return instructions

    def generate_balanced_portfolio(self, market):

        # 1. Get fiat value of portfolio

        fiat_total = sum(asset['value'] for asset in self.assets.values())
        self.fiat_total = fiat_total

        # 2. Calculate balanced portfolio
       
        balanced_portfolio = {}
        remaining_weight = 1

        # 2.1 Hard handpicked
        
        for symbol in self.parameters['hard_hp']:
            balanced_portfolio[symbol] = self.parameters['hard_hp'][symbol]
            remaining_weight -= self.parameters['hard_hp'][symbol]
            self.parameters['banned'].append(symbol)

        # 2.2 Calculate remaining lots 

        dynamic_mcap = math.floor((self.parameters['profit_level'] * fiat_total * remaining_weight)/self.parameters['min_trade'])
        free_lots = min(
            max((self.parameters['min_coins']-len(balanced_portfolio)), dynamic_mcap),
            self.parameters['max_coins']-len(balanced_portfolio))
        lot_size = remaining_weight/free_lots

        # 2.2.1 Deal with weighted param
            # if weighted > 0: calc with weighted = 1
            # if weighted < 1: calc with weighted = 0
            # if weighted != 0 and weighted != 1, take corresponding weighted average
            # possible implementation with weighted < 0 and/or weighted > 1?

        # 2.3 Soft handpicked
        if self.parameters['soft_hp'] and free_lots > 0:
            for symbol in self.parameters['soft_hp']:
                balanced_portfolio[symbol] = lot_size
                self.parameters['banned'].append(symbol)
                free_lots -= 1

        # 2.4 Market cap coins
        skipped = None
        index = 0
        while free_lots > 0 and index < len(market):
            symbol = market[index]['symbol']
            if skipped:
                balanced_portfolio[skipped] = lot_size
                free_lots -= 1
                self.parameters['banned'].append(symbol)
                skipped = None
                continue
            if symbol not in self.parameters['banned']:
                # Checking for wiggle (almost as good coin):
                if symbol not in self.assets.keys() and self.parameters['wiggle'] > 0:
                    next_index = index + 1
                    next_symbol = market[next_index]['symbol']
                    while (market[next_index]['mcap'] > (1-self.parameters['wiggle'])*market[index]['mcap']):
                        if (next_symbol not in self.parameters['banned'] and next_symbol not in self.assets.keys()):
                            skipped = symbol
                            symbol = next_symbol
                        next_index += 1
                        
                balanced_portfolio[symbol] = lot_size
                free_lots -= 1
                self.parameters['banned'].append(symbol)
            index += 1

        balanced_portfolio = {symbol : {'fiat' : balanced_portfolio[symbol]*fiat_total, 'pct': balanced_portfolio[symbol], 'tokens': balanced_portfolio[symbol]*fiat_total/(float(self.assets[symbol]['last_price']) if symbol in self.assets.keys() else [coin['last_price'] for coin in market if coin['symbol'] == symbol][0]) ,'price': float(self.assets[symbol]['last_price']) if symbol in self.assets.keys() else [coin['last_price'] for coin in market if coin['symbol'] == symbol][0]} for symbol in balanced_portfolio}

        self.balanced_portfolio = balanced_portfolio

        return balanced_portfolio

    def generate_diff_matrix(self, balanced_portfolio, market):
        diffs = {}
        for symbol in balanced_portfolio:
            try:
                diffs[symbol] = (self.assets[symbol]['value'] - balanced_portfolio[symbol]['fiat'])
            except KeyError:   
                diffs[symbol] = - balanced_portfolio[symbol]['fiat']
        for symbol in self.assets:
            if symbol not in diffs.keys():
                diffs[symbol] = self.assets[symbol]['value']
        for symbol in diffs:
            price = balanced_portfolio[symbol]['price'] if symbol in balanced_portfolio.keys() else [coin['last_price'] for coin in market if coin['symbol'] == symbol][0]
            diffs[symbol] = {'fiat': diffs[symbol], 'tokens': diffs[symbol]/price, 'price': price}
        self.diff_matrix = diffs
        return diffs
        
    def parse_parameters(self, parameters):

        parsed_parameters = {}
        
        # String parameters
        parsed_parameters['denominator'] = parameters['denominator']

        # Float parameters
        for param in ['weighted', 'wiggle', 'min_trade_abs', 'min_trade', 'profit_level']:
            parsed_parameters[param] = float(parameters[param]) if parameters[param] else None
        
        # Integer parameters
        parsed_parameters['min_coins'] = int(parameters['min_coins']) if parameters['min_coins'] else 0
        parsed_parameters['max_coins'] = int(parameters['max_coins']) if parameters['max_coins'] else math.inf


        # List of string parameters
        for param in ['banned', 'soft_hp']:
            parsed_parameters[param] = parameters[param].split(',') if parameters[param] else []

        # Dict
        for param in ['hard_hp']:
            parsed_parameters[param] = ast.literal_eval(parameters[param]) if parameters[param] else {}

        return parsed_parameters