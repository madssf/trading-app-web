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
  GET Portfolios/Owner=User
  GET Watchlists/Owner=User

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

#### stats/graphs

Current pie chart

- Needed endpoints:
  GET PortfolioID/Assets=Active

Performance graph

- Needed endpoints:
  GET PortfolioID/Assets=All
  GET PortfolioID/Deposits
  GET MCAP History/startime

History graph

- Needed endpoints:
  GET PortfolioID/Assets=All

### USER WATCHLIST VIEW

#### Watchlist list view

GET User/Watchlists

#### Watchlist detail view

GET WatchlistCurrencies + currency details
POST WatchlistCurrency

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

- Currency list
  GET currencies

- Currency detail
  GET currency+currencytags
  POST currencytag

- Tag group list
  POST taggroups

- Tag group detail
  GET taggroup+tags

- Tags list
  GET tags
  POST tag
- Tags detail
  POST taggroup

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
