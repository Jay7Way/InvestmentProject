import csv
import json
import pandas as pd

for i in range(1):
    answer_1 = input("Do you want to add an account? (Y/N)").upper()

    if answer_1 != "Y":
        ""
    else:
        fields = [input("Please insert name: "),
                  str(input("Please insert ID: ")),
                  input("Please insert balance: "),
                  [{input('Please insert starting stock: ').upper(), input('Please insert quantity of this stock: ')}],
                  []]

        df = pd.read_csv('ACCOUNT_DATA.csv')
        with open('ACCOUNT_DATA.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        df = pd.read_csv('ACCOUNT_DATA.csv')
        print(df)


