from scripts.db import DBConnection
import time
import argparse
from tqdm import tqdm
from platform import platform
from getpass import getpass

print("Price-updater, log in with Django credentials:")
username = input("Username: ")
password = getpass()

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', "--interval",
    help='wait time between invokes in minutes, default 10 minutes', type=int)

args = parser.parse_args()

INTERVAL = args.interval*60 if args.interval else 10*60

context = {'source': f'scheduler: {platform()}'}


db = DBConnection(username, password)


while True:
    startup_string = f'starting scheduled run | interval: {int(INTERVAL/60)} min'
    print(startup_string)
    try:
        print("invoking...")
        db.update_currencies()

    except (KeyError) as e:
        print(f'Error: {e}')

    for i in tqdm(range(INTERVAL), desc="[Ctrl+C to quit] - waiting"):
        time.sleep(1)
    print('scheduled run complete...')
