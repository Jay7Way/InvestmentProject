
from Classes.Stock import Stock
from Classes.Order import Order
from Classes.Order import Buy
from Classes.Order import Sell



class Account:



    def __init__(self, name, id, balance, portfolio, sells, buys):
        self.name = name
        self.id = id
        self.balance = balance
        self.portfolio = portfolio
        self.portfolio = {
            "Name": Stock.name,
            "Number of stock": 0
        }
        self.orders = {
        "Buys": buys,
        "Sells": sells,
        }

    def AddStock(self, name, number):
        self.portfolio.append({"Name:": name,
        "Number of stock": number}
        )


    def AddBuy(self, buys):
        self.orders.append({"Buys": buys}
        )

