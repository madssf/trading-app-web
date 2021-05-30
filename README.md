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

```sql
SELECT * FROM PORTFOLIOS JOIN PORTFOLIO_PARAMETERS JOIN PORTFOLIO_CREDENTIALS JOIN PORTFOLIO_ASSETS
```

```json
  {portfolio: {
    strategy: 'name',
    parameters: {param1: value, param2: value},
    credentials: {key: string, secret: string}
    }
  }
```

### 2. Execute strategy

- GET: exchange - market data

```Python
for portfolio in portfolios:
  assets = get_assets(exchange='Binance', credentials)
  #change unlocked assets that differ from exchange
  strategy = Strategy(assets, parameters, market_data)
  strategy.instruct()
  if instructions: trade(instructions)
    # TODO:replace request with sql query
    request.post(trades)
  # due to staking
  if new_assets != old_assets:
    # TODO: check if stake expired
    # TODO:replace request with sql query
    email_user(trades)
    requests.post(trades)
# for performance comparison etc. only do this every hour etc.
# TODO:replace request with sql query
requests.post(total_mcap)
```
