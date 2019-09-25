from Functions.DataParser import dataParser
from Functions.AccountsCreator import accountsCreator
from Functions.MainFunctions import getAccount
from website import hello

traded_tickers=["AAPL", "GOOGL", "INTC", "MFST"]
MktInput = {"AAPL" : int(dataParser("AAPL", "latest"))}
# MktInput = MktInput.append {"GOOGL" : int(dataParser("GOOGL", "latest"))}
# MktInput = MktInput.append(dataParser("INTC", "history"))
# MktInput = MktInput.append(dataParser("MFST", "history"))
accList, df= accountsCreator(True)


cont = True
while (cont):
    #get and check name
    name=input("Who will trade?")
    index=getAccount(name, accList)
    while index is None:
        print("Name not found, try again.")
        name = input("Who will trade?")
        index = getAccount(name, accList)

    #get and check ticker
    ticker=input("Which Ticker?")
    while ticker not in traded_tickers:
        print("Not a valid ticker, try again:")
        ticker = input("Which Ticker?")

    #get quantity
    quant=int(input("How many stocks?"))


    prevBalance = accList[index].balance
    accList[index].balance-=MktInput[ticker]*quant
    print(name+" bought "+str(quant)+" of "+ticker+" at "+str(MktInput[ticker])+" each. Previous balance was " + str(prevBalance)+", new balance is: "+str(accList[index].balance))


    cont = input("Keep playing? Y/N").upper()
    if cont != 'Y':
        cont = False
print("Thanks for playing with us!")