#!python3
import json
import websocket
from config import *

# API_KEY ='PKG1MYWFMDV7RS2FK3FS'
API_KEY = 'VnTttV_0R_AoK_2LrJL__iPPud7fVw_6P__THA'
TICKERS = "Q.MSFT"

socket = "wss://socket.polygon.io/stocks"

def on_open(ws):
    print('hola mundo')

    auth_data = {
        
        "action":"auth",
        "params": API_KEY

    }
    ws.send(json.dumps(auth_data))
    channel_data = {
        "action":"subscribe",
	    "params":"T.MSFT,T.AAPL,T.AMD,T.NVDA"
    }
    ws.send(json.dumps(channel_data)
    )
def on_close(ws,message):
    print('chau mundo')    


def on_message(ws,message):
    print('recibe mensaje')
    print(message)

# websocket.enableTrace(True)

ws = websocket.WebSocketApp(socket,on_message=on_message, on_close=on_close , on_open=on_open)

ws.run_forever()