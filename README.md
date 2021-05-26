# trading-app-web

django, react

https://saasitive.com/tutorial/react-token-based-authentication-django/

## Cloud Script

_Only Binance for now, makes dealing with market data easier_

### 1. Django Request/DB query

- GET: all portfolios with a strategy

```json
  {portfolio: {
    strategy: 'name',
    parameters: {param1: value, param2: value},
    assets: {symbol: {tokens: float, avg: float}},
    credentials: {key: string, secret: string}
    }
  }
```

### 2. Execute strategy

- GET: exchange - market data

```Python
for portfolio in portfolios:
  strategy = Strategy(assets, parameters, market_data)
  strategy.instruct()
  if instructions: trade(instructions)
    request.post(trades)
  # due to staking
  if new_assets != old_assets:
    # logic: check if stake expired
    requests.post(trades)
# for performance comparison etc.
requests.post(total_mcap)
```

## Backend TODO:

### Short-term:

- Permissions on everything
- Linked API views, relational

### Mid-term:

- PortfolioAssets status Enum
- Parameters that use coins should have coin as FK

### Long-term:

- Store prices in DB
