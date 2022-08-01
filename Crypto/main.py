from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
from time import sleep

def api_automate():
  global df
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start': '1',
    'limit': '15',
    'convert': 'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'ad808a91-2901-4903-98a8-39e7c9f6e859',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  df = pd.json_normalize(data['data'])
  df['timestamp'] = pd.to_datetime('now')

  if not os.path.isfile(r'C:\Users\44773\PycharmProjects\Crypto\data\API.csv'):
    df.to_csv(r'C:\Users\44773\PycharmProjects\Crypto\data\API.csv', header='column_names')
  else:
    df.to_csv(r'C:\Users\44773\PycharmProjects\Crypto\data\API.csv', mode='a', header=False)

#The limit on my account is 333 calls per day
for i in range(333):
  api_automate()
  print('API Automation Completed')
  sleep(100)
exit()