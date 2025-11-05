from tarfile import data_filter
import requests
import os
from dotenv import load_dotenv
load_dotenv()
import time
import csv


MASSIVE_API_KEY = os.getenv('MASSIVE_API_KEY')
print('Hello World')
print(MASSIVE_API_KEY)

LIMIT = 1000 #smaller batch size to avoid rate limits

url = f'https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={MASSIVE_API_KEY}'
response = requests.get(url)
tickers = [] # list of tickers


data = response.json()
for ticker in response.json()['results']:
    tickers.append(ticker)

while 'next_url' in data:
    print('requesting next page', data['next_url'])
    response = requests.get(data['next_url'] + f'&apiKey={MASSIVE_API_KEY}')
    data = response.json()
    print(data)
    if 'results' in data:
        for ticker in data['results']:
            tickers.append(ticker)
    else:
        print('no results found')

print(len(tickers))
    
example_ticker = {
    'ticker': 'HOTH',
     'name': 'Hoth Therapeutics, Inc. Common Stock',
      'market': 'stocks',
       'locale': 'us',
        'primary_exchange': 'XNAS', 
        'type': 'CS', 
        'active': True,
         'currency_name': 'usd',
          'cik': '0001711786',
           'composite_figi': 'BBG00H0HZ8S8',
            'share_class_figi': 'BBG00H0HZ8T7',
             'last_updated_utc': '2025-11-04T07:06:14.176512988Z'
             }

# Write tickers to CSV with the same schema as example_ticker
csv_filename = 'tickers.csv'
fieldnames = ['ticker', 'name', 'market', 'locale', 'primary_exchange', 'type', 
              'active', 'currency_name', 'cik', 'composite_figi', 'share_class_figi', 
              'last_updated_utc']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ticker in tickers:
        # Ensure all fields from example_ticker schema are included
        row = {}
        for field in fieldnames:
            row[field] = ticker.get(field, '')
        writer.writerow(row)

print(f'Successfully wrote {len(tickers)} tickers to {csv_filename}')
