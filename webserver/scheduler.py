from scripts import lambda_func
from time import sleep
import argparse
from tqdm import tqdm
from platform import platform


parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', "--interval",
    help='wait time between invokes in minutes, default 15 minutes', type=int)

args = parser.parse_args()

INTERVAL = args.interval*60 if args.interval else 15*60


while True:
    print(f'starting scheduled run | interval: {int(INTERVAL/60)} min')
    lambda_func.lambda_handler({'source': platform()})
    for i in tqdm(range(INTERVAL), desc="[Ctrl+C to quit] - waiting"):
        sleep(1)
    print('scheduled run complete...')
