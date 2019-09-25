from Functions.DataParser import dataParser
from Functions.AccountsCreator import accountsCreator
from Functions.MainFunctions import getAccount
from Functions.MainFunctions import getStock
from Functions.MainFunctions import BuyStock
from Stock import Stock

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
    index_Acc=getAccount(name, accList)
    while index_Acc is None:
        print("Name not found, try again.")
        name = input("Who will trade?")
        index_Acc = getAccount(name, accList)

    #get and check ticker
    ticker=input("Which Ticker?")
    index_Stock=getStock(ticker, traded_tickers)
    while index_Stock is None:
        print("Not a valid ticker, try again:")
        ticker = input("Which Ticker?")
        index_Stock = getStock(ticker, traded_tickers)

    #get quantity
    quant=int(input("How many stocks?"))

    #call buy/sell funciton
    prevBalance = accList[index_Acc].balance
    #accList[index_Acc].balance -= traded_stocks[index_Stock].current_price * quant
    # TODO
    accList[index_Acc].balance = BuyStock()
    print(name+" bought "+str(quant)+" of "+ticker+" at "+str(traded_stocks[index_Stock].current_price)+" each. Previous balance was " + str(prevBalance)+", new balance is: "+str(accList[index_Acc].balance))

    t+=1
    cont = input("Keep playing? Y/N").upper()
    if cont != 'Y':
        cont = False
print("Thanks for playing with us!")