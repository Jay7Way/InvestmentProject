
from Classes.Stock import Stock
from Classes.Order import Buy, Sell

class Account:

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

    def AddStock(self, ticker, quantity):
        stockName = Stock.Name(ticker)
        self.portfolio.append({"Name:": stockName,
        "Number of stock": quantity}
        )

    def RemoveStock(self, ticker, quantity):
        stockName = Stock.Name(ticker)
        if stockName in self.portfolio.keys():
            if self.portfolio[stockName] > quantity:
                self.portfolio[stockName] = self.portfolio[stockName] - quantity
                return 0
            else:
                self.portfolio.remove(stockName)
                print("Account holder not own this many stocks, we could only sell:"
                      , quantity - self.portfolio[stockName])
                return quantity - self.portfolio[stockName]
        else:
            print("Account holder does not own any of this stock")

    def BuyStock(self, ticker, quantity):
        self.balance +=  self.balance + Buy(ticker, quantity, "", Stock.Price(ticker))
        self.AddStock(ticker, quantity)

    def SellStock(self, ticker, quantity):
        self.balance +=  self.balance + Sell(ticker, quantity, "", Stock.Price(ticker))
        self.RemoveStock(ticker, quantity)


