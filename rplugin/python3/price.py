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
        response = requests.get(url, params=params)
        data = response.json()
        price = int(float(data["data"]["priceUsd"]))
        # use command to define var
        self.vim.command("let g:btc_price={}".format(price))
