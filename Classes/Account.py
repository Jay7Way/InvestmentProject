
from Classes.Stock import Stock
from Classes.Order import Buy, Sell, Order


class Account:

    # portfolio = {
    #     "Name": Stock.name,
    #     "Number of stock": 0
    # }
    #
    # orders = {
    #     "Buys": Buy,
    #     "Sells": Sell,
    # }

    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance


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
        price = Stock.getprice(ticker)
        if self.balance > Order.totalCost(Order(ticker, quantity, price)):
            self.balance += self.balance + Buy.totalCost(Buy(ticker, quantity, price))
            self.AddStock(ticker, quantity)
        else:
            Exception("Insufficient funds in the account to process this purchase")

    def SellStock(self, ticker, quantity):
        self.balance +=  self.balance + Sell.totalCost(Sell(ticker, quantity, Stock.getprice(ticker)))
        remaining = self.RemoveStock(ticker, quantity)
        print("There are ", remaining, " stocks left unsold")


# account1 = Account("AccountHolder1", "007", 10000, "", "", "")
#
# print(account1.balance)
#
# account1.BuyStock("AAPL", 10)
#
# print(account1.balance)

