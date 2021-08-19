from .config import Superuser
from .db import DBConnection
from .strategies.MCAPRebalancer import MCAPRebalancer


def main():
    db = DBConnection(Superuser.USERNAME, Superuser.PASSWORD)
    market = db.update_currencies()
    db.update_exchange_assets()
    portfolios = db.get_strategy_portfolios()
    instructions_list = []
    emails_list = []
    trades_list = []
    for portfolio in portfolios:
        if len(portfolio['assets']) > 0:
            strategy = MCAPRebalancer(
                portfolio['strategy']['parameters'], portfolio['assets'])
            instructions = strategy.instruct(market)
            
            if instructions:
                email_notify =  sorted(x['symbol'] for x in instructions) != sorted(x['symbol'] for x in portfolio['strategy']['instructions']) and portfolio['email_notify'] if portfolio['strategy']['instructions'] else True
                instructions_list.append({'id': portfolio['id'], 'email': portfolio['email'] if email_notify else False, 'execute_trades': portfolio['execute_trades'], 'instructions' : instructions, 'balanced_portfolio': strategy.balanced_portfolio, 'diff_matrix': strategy.diff_matrix})
            else:
                instructions_list.append({'id': portfolio['id'], 'email': False, 'execute_trades': False, 'instructions' : [], 'balanced_portfolio': strategy.balanced_portfolio, 'diff_matrix': strategy.diff_matrix})

    if len(instructions_list) > 0:
        db.update_instructions(instructions_list)
    for portfolio in instructions_list:
        if portfolio['email']:
            db.email_notify(portfolio)

if __name__ == "__main__":
    main({'source': 'main function - commmand line'})


def lambda_handler(context):
    '''
    : param context: {'source': string} optional: timeoffset
    : param event: backend.cmc_market_data()
    '''
    print(f"lambda_func.py invoked | context: {context}")

    main()
