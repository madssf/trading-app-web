import api_conn

token = api_conn.get_token()


data = api_conn.get_portfolios(token)

print(data)
