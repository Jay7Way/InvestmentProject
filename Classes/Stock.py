class Stock:
    name = ""
    price = 0
    #ask = 0
    #curr = "Eur"
    #bid = ""
    ticker = ""

    def __init__(self, price, name, ticker):
        self.price = price
        self.name = name
        self.ticker = ticker


    def Price(self, ticker):
        self.ticker = ticker
        return self.price