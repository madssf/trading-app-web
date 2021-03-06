# Before running scripts:

1. Go to /scripts/, make a file called 'config.py', add the following:

```python
import os

class Endpoints:
    # 8000 when running locally, 1337 with Docker/Nginx
    PORT = ["8000", "1337"]
    BASE = f"http://localhost:{PORT[1]}/api/v1/"
    LOGIN = BASE+"token/login"


class Parameters:
    # For coingecko
    BASE_FIAT = "USD"
    # Coins we don't need in our database, leave empty list if none.
    STABLECOINS = ['USDT', 'USDC', 'BUSD',
                   'TUSD', 'DAI', 'CUSDC', 'CDAI', 'CUSDC']


class Superuser:
    # Users for Django requests, needs to match /backend/project.env
    USERS = ['insert', 'usernames']
    PASSWORDS = ['insert', "passwords"]

```

2. Install requirements

```bash
cd scripts
# python 3
python3 -m virtualenv venv
source venv/bin/activate #deactivate to quit
pip install -r requirerments.txt

```

# Scripts

Make sure you are in /scripts/

## lambda_func.py

## db.py

```Python
db = DBConnection()
# Gets top 250 currencies from Coingecko and updates/creates records in database.
db.update_currencies()
# Gets all assets from all registered portfolio credentials and updates/creates records in database.
db.update_exchange_assets()

```
