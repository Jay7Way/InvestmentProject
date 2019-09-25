from Functions.DataParser import dataParser
from Classes.Account import Account
import pandas as pd

#MktInput = pd.DataFrame()

MktInput = dataParser("AAPL", "history")
MktInput = MktInput.append(dataParser("GOOGL", "history"))
MktInput = MktInput.append(dataParser("INTC", "history"))
MktInput = MktInput.append(dataParser("MFST", "history"))


#accList=[]
#AccountA = Account("Albert", 1, 20000)
#AccountB = Account("Ben", 2, 100000)
#AccountC = Account("Carl", 3, 50000)
#AccountD = Account("Dan", 4, 90000


Continue = 1
while (Continue):
    acc=input("Who will trade?")
    ticker=input("Which Ticker?")
    quant=input("How many stocks?")

    acc.makeTransaction()
    print(portfolio)
    Continue = input("Keep playing?")