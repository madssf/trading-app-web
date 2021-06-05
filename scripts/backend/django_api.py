import requests
from json import JSONDecodeError


class Api():

    def __init__(self, credentials, base_url, login_url):
        print(f"Creating new API connection for {credentials['username']}")
        self.base_url = base_url
        self.login_url = login_url
        self.token = None
        self.user = credentials['username']
        self.password = credentials['password']

    def login(self):
        if not self.token:
            print(f"Getting new token for {self.user}")
            creds = {'username': self.user,
                     'password': self.password}
            data = requests.post(self.login_url, data=creds)
            print(data)
            self.token = data.json()['auth_token']
            print(f"{self.user} logged in!")
        else:
            print(f"Already got token for user: {self.user}")

    def make_request(self, method, endpoint, data=None):
        if not self.token:
            self.login()
        if method == "GET":
            res = requests.get(self.base_url+endpoint, headers={
                'Authorization': f'Token {self.token}'})
        elif method == "POST":
            res = requests.post(self.base_url+endpoint, data=data,
                                headers={'Authorization': f'Token {self.token}', "content-type": "application/json"})
        elif method == "PATCH":
            res = requests.patch(self.base_url+endpoint, data=data, headers={
                'Authorization': f'Token {self.token}'})
        else:
            print(f"Method not recognized: {method} {endpoint}")
        try:
            res = res.json()
        except JSONDecodeError:
            res = {'error': 'JSONDecodeError', 'msg': res}
        print(f"Request: {method} {self.base_url}{endpoint} Data: {data}")
        print(f"Response: {res}")
        return res
