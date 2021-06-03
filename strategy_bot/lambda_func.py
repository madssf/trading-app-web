import backend

# Get portfolios from API
token = backend.get_token()
portfolios = backend.get_portfolios(token)

# Get market data
data = backend.get_market_data()


def main(context, market_data):
    data = portfolios
    print(data)


if __name__ == "__main__":
    main({'source': 'main function - cmd line'}, 0)


def lambda_handler(context, event):
    '''
    :param context: {'source': string} optional: timeoffset
    :param event: backend.cmc_market_data()
    '''
    print(f"lambda_func.py invoked | context: {context}")

    main(context, event)
