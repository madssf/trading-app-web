import backend

# Get portfolios from API

# Get market data


def main(context, market_data):
    pass


if __name__ == "__main__":
    main({'source': 'main function - cmd line'}, 0)


def lambda_handler(context, event):
    '''
    :param context: {'source': string} optional: timeoffset
    :param event: backend.cmc_market_data()
    '''
    print(f"lambda_func.py invoked | context: {context}")

    main(context, event)
