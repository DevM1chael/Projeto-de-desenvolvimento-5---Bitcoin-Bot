import websocket


def ao_abrir(ws):
    print("Conectado")

    json_subscribe = """
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    """

    ws.send(json_subscribe)

def ao_fechar(ws):
    print("Fechou a conexão!")

def erro(ws, erro):
    print("Deu erro!")
    print(erro)

def ao_receber_mensagem(ws, mensagem):
    print(mensagem)

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=ao_abrir,
                                on_message=ao_receber_mensagem,
                                on_error=erro,
                                on_close=ao_fechar)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    