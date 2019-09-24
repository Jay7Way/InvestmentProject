class Stock:
    name = ""
    ask = 0
    curr = "Eur"
    bid = ""
    ticker = ""

    def __init__(self, bid, ask, curr, name, ticker):
        self.bid = bid
        self.ask = ask
        self.curr = curr
        self.name = name
        self.ticker = ticker

