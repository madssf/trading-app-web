# trading-app-web

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

- GET: exchange - market data

```Python
for portfolio in portfolios:
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
# for performance comparison etc. only do this every hour etc.
requests.post(total_mcap)
```
