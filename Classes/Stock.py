class Stock:
    name = ""
    price = 0
    ticker = ""


    def __init__(self, price, name, ticker):
        self.price = price
        self.name = name
        self.ticker = ticker

    def getprice(self, ticker):
        self.ticker = ticker
        return self.price

    def Name(self, ticker):
        self.ticker = ticker
        return self.name

