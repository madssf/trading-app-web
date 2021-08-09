from .config import Superuser
from .db import DBConnection
from .strategies.MCAPRebalancer import MCAPRebalancer


def main():
    db = DBConnection(Superuser.USERNAME, Superuser.PASSWORD)
    market = db.update_currencies()
    db.update_exchange_assets()
    portfolios = db.get_strategy_portfolios()   
    for portfolio in portfolios:
        if len(portfolio['assets']) > 0:
            strategy = MCAPRebalancer(
                portfolio['strategy']['parameters'], portfolio['assets'])
            instructions = strategy.instruct(market)
            # check if instructions differ from previous instructions
                # do post request if different
            # snooze
            #
            if instructions:
                # db.post_instructions
                if portfolio['email_notify']:
                    # send email
                    pass
                if portfolio['execute_trades']:
                    # execute trades
                    pass


if __name__ == "__main__":
    main({'source': 'main function - commmand line'})


def lambda_handler(context):
    '''
    : param context: {'source': string} optional: timeoffset
    : param event: backend.cmc_market_data()
    '''
    print(f"lambda_func.py invoked | context: {context}")

    main()
