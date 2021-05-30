import requests
import config


def get_token():
    creds = {'username': config.API_USER, 'password': config.API_PASS}
    data = requests.post(config.TOKEN_URL, data=creds)
    return data.json()['auth_token']


def get_portfolios(token):
    data = requests.get(config.GET_URL, headers={
                        'Authorization': f'Token {token}'})
    # if token err: get new token
    return data.text
