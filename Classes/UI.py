

class Account(object):

    def __init__(self, name, id, balance, portfolio, orders):
        self.name = name
        self.id = id
        self.balance = balance
        self.portfolio = portfolio
        self.orders = orders


accounts = []
# Add account
def AddAccount(name, id, balance, portfolio, orders):
        accounts.append(name, id, balance, portfolio, orders)

answer_1 = input("Do you want to add an account? (Y/N)").upper()

if answer_1 != "Y":
    ""
else:
    AddAccount(name = input("Please insert name: "), id = input("Please insert ID: "), balance = input("Please insert balance: "), portfolio = [], orders = [])

print(accounts)