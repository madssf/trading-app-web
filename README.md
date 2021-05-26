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

## Cloud Script

_Only Binance for now, makes dealing with market data easier_

### DB query

```sql
SELECT * FROM PORTFOLIOS JOIN PORTFOLIO_PARAMETERS JOIN PORTFOLIO_CREDENTIALS
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

## Strategies/watchlist/research TODO:

### Short-term:

- Calculate beta and other metrics for portfolios.

### Mid-term:

- Get inspired by VORTECS and such for parameters for strategies.
- Research panel in front-end.
  - Twitter data,
  - Google trends etc.
  - Some news API
  - CoinmarketCal ish - also consider manually adding stuff here!
  - On-chain data, fees, txs etc.

### Long-term:

- Goal: All of the above should be usable as input in some strategy.

## Cloud Script TODO:

### Short-term:

- Write model code
- Write trading code

## Backend TODO:

### Short-term:

- Permissions on everything
- Change mcap_weigthed parameter:
  - Float 0 to 1, no weight to full weight
  - Some param for dealing with small caps
- Linked API views, relational

### Mid-term:

- PortfolioAssets status Enum
- Parameters that use coins should have coin as FK

### Long-term:

- Store prices in DB

## Frontend TODO:

### Short-term:

- Recreate streamlit dashboard
- Watchlists
