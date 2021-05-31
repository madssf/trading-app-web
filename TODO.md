## Strategies/watchlist/research:

### Short-term:

- Calculate beta and other metrics for portfolios.
- Some param for dealing with small caps when mcap_weighted = 1

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

## STRATEGY BOT:

### Short-term:

- Write model code
- Write trading code

## BACKEND:

### Short-term:

- Endpoints for frontend
- Remove unused endpoints
- Fix user endpoints permissions
- Table for currency stats (currency unique)

### Mid-term:

- Parameters that use coins should have coin as FK
- Figure out permissions on tags (users should be able to create tags, but need to keep order)
- Write tests
- Events model
- Table for stablecoins/general banned

### Long-term:

- Store prices in DB
- Allow users to make strategies and parameters

## FRONTEND:

### Short-term:

- Recreate streamlit dashboard
- Watchlists
