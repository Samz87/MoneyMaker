import websocket, json, pprint, talib, numpy, ta
import config
from datetime import datetimf
from binance.client import Client
from binance.enums import *

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

now = datetime.now()
closes = []
in_position = False

client = Client(config.API_KEY, config.API_SECRET, tld='com')

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print("Envoi de l'ordre")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        return False

    return True

def on_open(ws):
    print('Connexion établie')

def on_close(ws):
    print('Connexion fermée')

def on_message(ws, message):
    global closes
    
    current_time = now.strftime("%H:%M:%S")
    print("Nouveau message à", current_time)

    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("Candle fermé à {}".format(close))
        closes.append(float(close))
        print("Historique des fermetures :")
        print(closes)

        if len(closes) > config.RSI_PERIOD: 
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, config.RSI_PERIOD)
            print("Tous les RSI calculés :")
            print(rsi)
            last_rsi = rsi[-1]
            print("Le RSI actuel est {}".format(last_rsi))

            if last_rsi > config.RSI_OVERBOUGHT:
                if in_position:
                    print("Surachat! Vends tout!")
                    order_succeeded = order(SIDE_SELL, config.TRADE_QUANTITY, config.TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = False
                else:
                    print("Surachat mais tu n'en a pas à vendre, rien à faire.")

            if last_rsi < config.RSI_OVERSOLD:
                if in_position:
                    print("Survente mais tu en as deja, rien à faire.")
                else:
                    print("Survente! On achète!")
                    order_succeeded = order(SIDE_BUY, config.TRADE_QUANTITY, config.TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
