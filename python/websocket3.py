#!python3

#https://pypi.org/project/websocket_client/
import websocket
import requests

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    # auth_data = {"action":"auth","params": bqaj87frh5r8t7qna490}

    # ws.send(auth_data)
    # ws.send('{"type":"subscribe","symbol":"MSTF"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    # ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    # ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bqaj87frh5r8t7qna490",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    
    ws.on_open = on_open
    ws.run_forever()

a = requests.get('https://finnhub.io/api/v1/stock/peers?symbol=AMZN&token=bqaj87frh5r8t7qna490')
# print(a.json())
# [
#   "AAPL",
#   "EMC",
#   "HPQ",
#   "DELL",
#   "WDC",
#   "HPE",
#   "NTAP",
#   "CPQ",
#   "SNDK",
#   "SEG"
# ]

b = requests.get('https://finnhub.io/api/v1/stock/price-target?symbol=NFLX&token=bqaj87frh5r8t7qna490')
# print(b.json())

c = requests.get('https://finnhub.io/api/v1/quote?symbol=MSFT&token=bqaj87frh5r8t7qna490')
# print(c.json())
# {
#   "c": 261.74,Current price
#   "h": 263.31,High price of the day
#   "l": 260.68,Low price of the day
#   "o": 261.07,Open price of the day
#   "pc": 259.45,Previous close price
#   "t": 1582641000, Timestamp of current daily bar
# }

d = requests.get('https://finnhub.io/api/v1/stock/dividend?symbol=MSFT&from=2019-02-01&to=2020-02-01&token=bqaj87frh5r8t7qna490')
# print(d.json())
# Get dividends data for stocks.
# [
#   {
#     "symbol": "AAPL",
#     "date": "2019-11-07 14:30:00",
#     "amount": 0.77
#   },
#   {
#     "symbol": "AAPL",
#     "date": "2019-08-09 13:30:00",
#     "amount": 0.77
#   },
#   {
#     "symbol": "AAPL",
#     "date": "2019-05-10 13:30:00",
#     "amount": 0.77
#   },
#   {
#     "symbol": "AAPL",
#     "date": "2019-02-08 14:30:00",
#     "amount": 0.73
#   }
# ]
