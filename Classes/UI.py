from Classes.Account import Account

accounts = []
# Add account
class AddAccount(object):
    answer_1 = input("Do you want to add an account? (Y/N)").upper()

    if answer_1 != "Y":
        exit
    else:
        name = input("Please insert name: ")
        id = input("Please insert ID: ")
        balance = input("Please insert balance: ")
        portfolio = []
        orders = []
        accounts.append(Account(name, id, balance, portfolio, orders))

