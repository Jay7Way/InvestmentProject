from Functions.DataParser import dataParser
from Functions.AccountsCreator import accountsCreator
from Functions.MainFunctions import getAccount
from Classes.Stock import Stock

traded_tickers=["AAPL", "GOOGL", "INTC", "MFST"]
traded_tickers=["AAPL", "GOOGL"] #temp small set

AAPL_history = dataParser("AAPL", "history")
GOOGL_history = dataParser("GOOGL", "history")
# MktInput = MktInput.append(dataParser("INTC", "history"))
# MktInput = MktInput.append(dataParser("MFST", "history"))
accList, df= accountsCreator(True)

apple = Stock(AAPL_history[-1], "Apple", "AAPL", AAPL_history)
google = Stock(GOOGL_history[-1], "Google", "GOOGL", GOOGL_history)
traded_stocks=[apple, google]

cont = True
t=1
while (cont):
    #update prices
    for i in range(0,len(traded_stocks)):
        traded_stocks[i].update_price(t)
        print("Todays price of "+traded_stocks[i].name+" is "+str(traded_stocks[i].current_price))

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

    #call buy/sell funciton
    make_trade() = update_client_portfolio()

    prevBalance = accList[index].balance
    accList[index].balance-=todaysPrices[ticker]*quant
    print(name+" bought "+str(quant)+" of "+ticker+" at "+str(todaysPrices[ticker])+" each. Previous balance was " + str(prevBalance)+", new balance is: "+str(accList[index].balance))

    t+=1
    cont = input("Keep playing? Y/N").upper()
    if cont != 'Y':
        cont = False
print("Thanks for playing with us!")