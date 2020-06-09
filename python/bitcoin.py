# 47fa7d9b-ef9d-4133-85b4-c9dca5fb1010

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# import pyfiglet module 
import pyfiglet 

result = pyfiglet.figlet_format("Geeks", font = "doh" ) 
print(result) 

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '47fa7d9b-ef9d-4133-85b4-c9dca5fb1010',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
  print('precio en dolares: '+str(data['data'][0]['quote']['USD']['price']))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)