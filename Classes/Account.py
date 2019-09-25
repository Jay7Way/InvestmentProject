from .Stock import Stock

class Account:

    def __init__(self, name, id, balance, portfolio, orders):
        self.name = name
        self.id = id
        self.balance = balance
        self.portfolio = portfolio
        self.orders = orders

    portfolio = {
        "Name": Stock.name,
        "Number of stock": 0
    }

    orders = {
        "Buys": 0,
        "Sells": 0,
    }
