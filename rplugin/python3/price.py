from datetime import datetime
from time import sleep

import pynvim
import requests


@pynvim.plugin
class Price(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.function("Stocks")
    def stock_function_handler(self, args):
        url = "http://api.coincap.io/v2/assets/bitcoin"
        params = {"exchangeId": "okex", "baseSymbol": "BTC", "quoteSymbol": "USDT"}
        try:
            response = requests.get(url, params=params)
            data = response.json()
            price = int(float(data["data"]["priceUsd"]))
            # use command to define var
            self.vim.command("let g:btc_price={}".format(price))
        except Exception as e:
            self.vim.command("let g:btc_price=-1")


if __name__ == "__main__":
    url = "http://api.coincap.io/v2/assets/bitcoin"
    params = {"exchangeId": "okex", "baseSymbol": "BTC", "quoteSymbol": "USDT"}
    while True:
        response = requests.get(url, params=params)
        data = response.json()
        price = int(float(data["data"]["priceUsd"]))
        print("{} {}".format(datetime.now(), price))
        sleep(1)
