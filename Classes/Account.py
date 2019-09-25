from Classes.Stock import Stock
from Classes.Order import Buy, Sell

class Account(object):

    portfolio = {
        "Name": Stock.name,
        "Number of stock": 0
        }

    orders = {
        "Buys": Buy,
        "Sells": Sell,
    }

    def __init__(self, name, id, balance, portfolio, sells, buys):
        self.name = name
        self.id = id
        self.balance = balance
        self.portfolio = portfolio
        self.orders = sells, buys

    def AddStock(self, name, number):
        self.portfolio.append({"Name:": name,
        "Number of stock": number}
        )

    def BuyStock(self, ticker, quantity):
        self.balance +=  self.balance + Buy(ticker, quantity, "", Stock.Price(ticker))
        self.portfolio.append(ticker, quantity)

    def SellStock(self, ticker, quantity):
        self.balance +=  self.balance + Sell(ticker, quantity, "", Stock.Price(ticker))
        self.portfolio.remove(ticker, quantity)


