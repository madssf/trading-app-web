# trading-app-web

## Backend:

1.

```bash
cd backend
# python 3
python3 -m virtualenv venv
source venv/bin/activate #deactivate to quit
pip install -r requirerments.txt
cd server
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```

## Tech stack:

- Django, React, Python, PostgreSQL

## Business goals:

- Make coin research easier and social
- Automated trading strategies based on research
- Ability to have your portfolio use other peoples strategies
- Staking optimizing
- Minimizing market risk
- Encouraging fundamental view and hodling???

## Strategy Bot

_Only Binance for now, makes dealing with market data easier_

### 1. API request

```json
  {portfolio: {
    strategy: 'name',
    parameters: {param1: value, param2: value},
    assets: {exchange: {locked, flex, spot}},
    credentials: {key: string, secret: string}
    }
  }
```

### 2. Execute strategy

- GET: coingecko - mcap data
- GET: exchange - market data

```Python
def get_market_data():
  market_data = cg.list_market()
  market_data += #  # get prices for coins that were not in top 250
  write_to_db()

def write_to_db()
  request.post(mcap_total)
  request.post(market_data)


for portfolio in portfolios:
  if market_data.time > 5 min old: #get new market data if old
    get_market_data(write_mcap_total = False)
  # TODO: check if stake expired
  assets = get_assets(exchange='Binance', credentials)
  #change assets that differ from exchange, set update_assets = True
  strategy = Strategy(assets, parameters, market_data)
  strategy.instruct()
  if instructions:
    if portfolio_trade_activated:
      trade(instructions)
      request.post(trades)
      email_user(trades)
      update_assets = True
    else:
      email_user(instructions)
  if update_assets:
    request.post(new_assets)

```
