
from Classes.Market import Market
from Classes.Account import Account



for i in range (2):
    answer_1 = input("Do you want to add an account? (Y/N)").upper()

    if answer_1 != "Y":
        ""
    else:
        Market.AddAccount(name = input("Please insert name: "), id = input("Please insert ID: "), balance = input("Please insert balance: "), portfolio = Account.portfolio, orders = Account.orders)


print(Market.accounts)
