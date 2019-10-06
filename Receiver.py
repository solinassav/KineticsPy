# Import
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    pass


class Receiver(object):
    def __init__(self, adress):
        self.receive(adress)

    def receive(self, adress):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(adress,
                                  on_message = on_message,
                                  on_error = on_error,
                                  on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()