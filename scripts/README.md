_Only Binance for now, makes dealing with market data easier_

# Before running scripts:

1. Go to /scripts/, make a file called 'config.py', add the following:

```python
import os

class Endpoints:
    # 8000 when running locally, 1337 with Docker/Nginx
    PORT = ["8000", "1337"]
    BASE = f"http://localhost:{PORT[1]}/api/v1/"
    LOGIN = BASE+"token/login"


class Parameters:
    # For coingecko
    BASE_FIAT = "USD"
    # Coins we don't need in our database, leave empty list if none.
    STABLECOINS = ['USDT', 'USDC', 'BUSD',
                   'TUSD', 'DAI', 'CUSDC', 'CDAI', 'CUSDC']


class Superuser:
    # Users for Django requests
    USERS = ['insert', 'usernames']
    PASSWORDS = ['insert', "passwords"]

```

2. Install requirements

```bash
cd scripts
# python 3
python3 -m virtualenv venv
source venv/bin/activate #deactivate to quit
pip install -r requirerments.txt

```

# Scripts

Make sure you are in /scripts/

## lambda_func.py

## db.py

## Strategies

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
