from websocket import create_connection

import websocket
import _thread
import time
import rel

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_message(ws, message):
    print("message recu")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

ws = websocket.WebSocketApp(SOCKET,on_open=on_open,on_close=on_close,on_message=on_message)

ws.run_forever()

