

import re
import json
from typing import Reversible


class AssetBatchParser:

    def parse_binance_txt(data):
        temp = data['data'].split('\n')
        res = []
        for i in range(len(temp)):
            if 'Redeem earlier' in temp[i]:
                symbol = temp[i-6]
                info = temp[i-5].split('\t')
                res.append({
                    'symbol': symbol,
                    'amount': info[0],
                    'apr': float(info[1].strip('%'))/100,
                    'stake_start': info[2],
                    'stake_end': info[4]

                })

        return res

        # print(lines)
