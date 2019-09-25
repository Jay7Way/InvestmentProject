#import MarketOperator
import csv
import pandas as pd
from Classes.Market import Market
from Classes.Account import Account



for i in range (1):
    answer_1 = input("Do you want to add an account? (Y/N)").upper()

    if answer_1 != "Y":
        ""
    else:
        fields = [input("Please insert name: "), input("Please insert ID: "), input("Please insert balance: "), input('Please insert starting portfolio: '), []]

        with open('ACCOUNT_DATA.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

df = pd.read_csv('ACCOUNT_DATA.csv')
print(df)
