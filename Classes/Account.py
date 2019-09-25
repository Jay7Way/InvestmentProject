
from Classes.Stock import Stock
from Classes.Order import Buy, Sell, totalCost, Order


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
        self.orders = sells, buys

    def AddStock(self, ticker, quantity):
        stockName = Stock.Name(ticker)
        if stockName in self.portfolio.keys():
            self.portfolio[stockName] = self.portfolio[stockName] + quantity
        else:
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
                      , self.portfolio[stockName], "of this stock" )
                return quantity - self.portfolio[stockName]
        else:
            print("Account holder does not own any of this stock")

    def BuyStock(self, ticker, quantity):
        if self.balance > totalCost(Order(ticker, quantity, Stock.Price(ticker))):
            self.balance += self.balance + totalCost(Buy(ticker, quantity, Stock.Price(ticker)))
            self.AddStock(ticker, quantity)
        else:
            Exception("Insufficient funds in the account to process this purchase")

    def SellStock(self, ticker, quantity):
        self.balance +=  self.balance + totalCost(Sell(ticker, quantity, Stock.Price(ticker)))
        remaining = self.RemoveStock(ticker, quantity)
        print("There are ", remaining, " stocks left unsold")


account1 = Account("AccountHolder1", "007", 10000, "", "", "")

account1.BuyStock("AAPL",10)


