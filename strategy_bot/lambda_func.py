import backend

# Get portfolios from API
token = backend.get_token()
portfolios = backend.get_portfolios(token)

# Get market data
data = backend.get_market_data()


print(data)
