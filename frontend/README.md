# Frontend

## Views

### USER HOME VIEW

- User resources:

  - Portfolios
  - Watchlists

- Explore:

  - Watchlists
  - Currencies
  - Strategies
  - Portfolios
  - Research/resources

- Needed endpoints:
  GET User/Portfolios
  GET User/Watchlists

### USER PORTFOLIO VIEW

#### Current portfolio view

- Needed endpoints:
  GET PortfolioID/Assets=Active
  GET PortfolioID/Strategy+StrategyParameters

#### Portfolio manual inputs

- Needed enpoints:
  POST PortfolioID/Asssets
  POST PortfolioID/Deposits
  POST PortfolioID/Credentials
  POST PortfolioID/Strategy
  POST PortfolioID/PortfolioParameter

#### Performance and history stats/graphs

Performance graph

- Needed endpoints:
  GET PortfolioID/Assets=All
  GET PortfolioID/Deposits
  GET MCAP History/startime

History graph

- Needed endpoints:
  GET PortfolioID/Assets=All

### USER WATCHLIST VIEW

GET User/Watchlists/WatchlistCurrencies

### EXPLORE STRATEGIES VIEW

- Needed endpoints:
  GET Strategies/StrategyParameters

### EXPLORE PORTFOLIOS VIEW

#### Portfolio list view

- Needed endpoints:
  GET Portfolios/Public=True/Assets/Strategy

#### Portfolio detail view

- Needed endpoints:
  See performance graph

### EXPLORE CURRENCIES/TAGS VIEW

- Needed endpoints:
  GET currencies+tags
  GET taggroups+tags
  POST currencytag
  POST tag
  POST taggroups

### EXPLORE WATCHLISTS VIEW

- Needed endpoints:
  GET Watchlists/WatchlistCurrencies

### RESEARCH RESOURCES VIEW

- Upcoming events data
- Social platform data
  - Twitter data
  - Google Trends data
  - Reddit
- News data
