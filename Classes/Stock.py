class Stock:
    name = ""
    price = 0
    #ask = 0
    #curr = "Eur"
    #bid = ""
    ticker = ""

    def __init__(self, price, name, ticker):
        #self.bid = bid
        #self.ask = ask
        #self.curr = curr
        self.price = price
        self.name = name
        self.ticker = ticker

