from Functions.DataParser import dataParser
from Functions.AccountsCreator import accountsCreator
from Functions.MainFunctions import getAccount

traded_tickers=["AAPL", "GOOGL", "INTC", "MFST"]
AAPL_history = dataParser("AAPL", "history")
# MktInput = MktInput.append {"GOOGL" : int(dataParser("GOOGL", "latest"))}
# MktInput = MktInput.append(dataParser("INTC", "history"))
# MktInput = MktInput.append(dataParser("MFST", "history"))
accList, df= accountsCreator(True)


cont = True
t=1
while (cont):
    todaysPrices = {"AAPL": AAPL_history[-t]}
    print("Todays price of AAPL is "+str(todaysPrices["AAPL"]))
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
    accList[index].balance-=todaysPrices[ticker]*quant
    print(name+" bought "+str(quant)+" of "+ticker+" at "+str(todaysPrices[ticker])+" each. Previous balance was " + str(prevBalance)+", new balance is: "+str(accList[index].balance))

    t+=1
    cont = input("Keep playing? Y/N").upper()
    if cont != 'Y':
        cont = False
print("Thanks for playing with us!")