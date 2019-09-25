import csv
import json
from Account import Account
import pandas as pd

def accountsCreator(use_predefined):
    if use_predefined:
        accList=[]
        accountA = Account("Albert", 1, 20000)
        accList.append(accountA)
        accountB = Account("Ben", 2, 100000)
        accList.append(accountB)
        accountC = Account("Carl", 3, 50000)
        accList.append(accountC)
        accountD = Account("Dan", 4, 90000)
        accList.append(accountD)

        df = pd.read_csv('ACCOUNT_DATA.csv')
        for acc in accList:
            fields = [acc.name, acc.id, acc.balance]
            with open('ACCOUNT_DATA.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fields)

        df = pd.read_csv('ACCOUNT_DATA.csv')
        # print(df)

        return accList, df
    else:
        create_new_account = True
        while create_new_account:


            fields = [input("Please insert name: "),
                      str(input("Please insert ID: ")),
                      input("Please insert balance: "),
                      [{str(input('Please insert starting stock: ')).upper(): int(input('Please insert quantity of this stock: '))}],
                      []]

            df = pd.read_csv('ACCOUNT_DATA.csv')
            with open('ACCOUNT_DATA.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                fields[3] = json.dumps(fields[3])
                writer.writerow(fields)

            df = pd.read_csv('ACCOUNT_DATA.csv')
            print(df)

            df = pd.read_csv('ACCOUNT_DATA.csv')
            s = df.loc[4,'PORTFOLIO']
            print(s)
            pf = json.loads(s)
            print(pf)

            answer = input("Do you want to add another account? (Y/N)").upper()
            if answer == 'Y':
                create_new_account = False


