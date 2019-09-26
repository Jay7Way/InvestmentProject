class Stock:
    name = ""
    current_price = 0
    ticker = ""

    def __init__(self, current_price, name, ticker, price_history):
        self.current_price = current_price
        self.name = name
        self.ticker = ticker
        self.price_history = price_history

    def get_current_price(self, ticker):
        self.ticker = ticker
        return self.current_price

    def Name(self, ticker):
        self.ticker = ticker
        return self.name

    def update_price(self, t):
        self.current_price=self.price_history[t]


# apple = Stock(name="Apple", price=10, ticker="AAPL")
