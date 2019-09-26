from .Stock import Stock

class Account:


    #
    # orders = {
    #     "Buys": Buy,
    #     "Sells": Sell,
    # }

    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance
        self.portfolio = {}


    def makeTransaction(self, stock, quantity, buyOrSell):
        price = stock.current_price
        stockTicker = stock.ticker
        if buyOrSell == 'BUY':
            if self.balance > price*quantity:
                self.balance -= price*quantity
                self.addStock(stock, quantity)
                print("Buying stock...")
            else:
                print("Insufficient funds in the account to process this purchase")
        else:
            if stockTicker in self.portfolio:
                if self.portfolio[stockTicker] > quantity:
                    self.balance += price*quantity
                    self.addStock(stock, -quantity)
                    print("Selling stock...")
                else:
                    print("Insufficient stocks in portfolio in the account to process this purchase")
            else:
                print("You don't own this stock")


    def addStock(self, stock, quantity):
        stockTicker = stock.ticker
        if stockTicker in self.portfolio.keys():
            self.portfolio[stockTicker] = self.portfolio[stockTicker] + quantity
        else:
            self.portfolio[stockTicker] = quantity


    def printPortfolio(self, stockList, traded_tickers):
        print("\nBalance of account "+self.name+" is " + str(self.balance) + " and value of portfolio is " + str(self.valueOfPortfolio(stockList, traded_tickers))+
                                                                             "\nPortfolio of account "+self.name+" is " + str(self.portfolio))

    def valueOfPortfolio(self, stockList, traded_tickers):
        from Functions.MainFunctions import getStockIndex
        value = 0
        for ticker in self.portfolio:
            index_stock = getStockIndex(ticker, traded_tickers)
            stock = stockList[index_stock]

            quantity = self.portfolio[ticker]
            price = stockList[index_stock].current_price
            value += price*quantity

        return value







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

