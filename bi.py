import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    print(f"Price: {data['c']}")  # 'c' = last price

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"WebSocket closed with code: {close_status_code}, message: {close_msg}")

def on_open(ws):
    print("WebSocket connection opened.")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://fstream.binance.com/ws/ethusdt@ticker",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
