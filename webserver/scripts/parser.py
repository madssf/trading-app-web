from backend.django_api import Api

from config import Superuser, Endpoints

import re
import json


class Parser():

    def __init__(self):
        self.api = Api(
            {'username': Superuser.USERS[1], 'password': Superuser.PASSWORDS[1]}, Endpoints.BASE, Endpoints.LOGIN)

    def parse_binance_txt(self, filename="data.txt"):
        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line.split("\n"))

        data = []

        for i in range(len(lines)):
            if 'Redeem earlier' in lines[i]:
                symbol = lines[i-6][0]
                info = lines[i-5][0].split('\t')
                data.append({
                    'symbol': symbol,
                    'amount': info[0],
                    'apr': float(info[1].strip('%'))/100,
                    'stake_start': info[2],
                    'stake_end': info[4]
                })
        return data
        # print(lines)


p = Parser()
print(p.parse_binance_txt())
