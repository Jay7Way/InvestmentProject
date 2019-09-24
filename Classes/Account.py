from Classes.Stock import Stock
from Classes.Order import Order
from Classes.Order import Buy
from Classes.Order import Sell



class Account(object):

    portfolio = {
        "Name": Stock.name,
        "Number of stock": 0
        }

    def __init__(self, name, id, balance, portfolio, sells, buys):
        self.name = name
        self.id = id
        self.balance = balance
        self.portfolio = portfolio
        self.orders = {
        "Buys": buys,
        "Sells": sells,
        }

    def AddStock(self, name, number):
        self.portfolio.append({"Name:": name,
        "Number of stock": number}
        )


    def AddBuy(self, buy):
        self.orders.append({"Buys": buy}
        )

