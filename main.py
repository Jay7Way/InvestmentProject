import threading
import webbrowser

from .Functions.DataParser import dataParser
from .Functions.AccountsCreator import accountsCreator
from .Functions.MainFunctions import getAccount
from .Functions.MainFunctions import getStockIndex

from .Stock import Stock

#traded_tickers=["AAPL", "GOOGL", "INTC", "MFST"]

traded_tickers=["AAPL", "GOOGL"] #temp small set
# MktInput = MktInput.append(dataParser("INTC", "history"))
# MktInput = MktInput.append(dataParser("MFST", "history"))

AAPL_history = dataParser("AAPL", "history")
GOOGL_history = dataParser("GOOGL", "history")
accList, df= accountsCreator(True)

name = loggedin_user

apple = Stock(AAPL_history[-1], "Apple", "AAPL", AAPL_history)
google = Stock(GOOGL_history[-1], "Google", "GOOGL", GOOGL_history)
traded_stocks=[apple, google]

# if this is empty we just go to the next day, if name not in AccList then log in again

# todo import account details
# todo import market details
# todo display in form stock prices
# TODO any trades today? - new webpage No -> update of the day, yes -> execute trade, update portfolio , any more trades? loop

# TODO implement account names only

cont = True
t=1
while (cont):
    #update prices
    marketString = ""
    for i in range(0,len(traded_stocks)):
        traded_stocks[i].update_price(t)
        marketString += ("Todays price of "+traded_stocks[i].name+" is "+str(traded_stocks[i].current_price)+". ")
    print(marketString)


    #todo new HTML page - you wanna play a game?
    play_game = website.play_game()
    #return bool
    if play_game:
        #get and check ticker
        website.form()
        ticker = website.stock
        index_Stock=getStockIndex(ticker, traded_tickers)
        while index_Stock is None:
            print("Not a valid ticker, try again:")
            website.form()
            ticker = website.stock
            index_Stock = getStockIndex(ticker, traded_tickers)

        #get and check quantity
        validQuant = False
        #initialise quant
        quant=None
        while not validQuant:
            try:
                quant = website.amount
                if quant <= 0:
                    print("You only trade in positives, try again, and be more positive:")
                else:
                    validQuant = True
            except:
                print("Not a valid number, try again:")


        #call buy/sell funkytown
        prevBalance = accList[index_Acc].balance
        #accList[index_Acc].balance -= traded_stocks[index_Stock].current_price * quant
        # TODO
        print('\nBefore the transaction:')
        accList[index_Acc].printPortfolio(traded_stocks, traded_tickers)
        accList[index_Acc].makeTransaction(traded_stocks[index_Stock], quant, website.buyOrSell)
        print('\nAfter the transaction:')
        accList[index_Acc].printPortfolio(traded_stocks, traded_tickers)


        cont = input("\nKeep playing? Y/N").upper()
        if cont != 'Y':
            cont = False
        #this else is if you just want to go through time
    else:
        accList[index_Acc].printPortfolio(traded_stocks, traded_tickers)

    t += 1

print("Thanks for playing with us!")