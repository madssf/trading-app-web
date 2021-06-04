## lambda_func.py

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
