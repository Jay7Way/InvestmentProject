from Functions.DataParser import dataParser
from Functions.AccountsCreator import accountsCreator
from Functions.MainFunctions import getAccount
from Functions.MainFunctions import getStockIndex
from Stock import Stock

traded_tickers=["AAPL", "GOOGL", "INTC", "MSFT"]
#traded_tickers=["AAPL", "GOOGL"] #temp small set

AAPL_history = dataParser("AAPL", "history")
GOOGL_history = dataParser("GOOGL", "history")
INTC_history = dataParser("INTC", "history")
MSFT_history = dataParser("MSFT", "history")
# MktInput = MktInput.append(dataParser("INTC", "history"))
# MktInput = MktInput.append(dataParser("MFST", "history"))
accList, df= accountsCreator(True)

apple = Stock(AAPL_history[-1], "Apple", "AAPL", AAPL_history)
google = Stock(GOOGL_history[-1], "Google", "GOOGL", GOOGL_history)
intel = Stock(INTC_history[-1], "Intel", "INTC", INTC_history)
microsoft = Stock(MSFT_history[-1], "Microsoft", "MSFT", MSFT_history)
traded_stocks=[apple, google, intel, microsoft]

cont = True
t=1
while (cont):
    #update prices
    marketString = ""
    for i in range(0,len(traded_stocks)):
        traded_stocks[i].update_price(t)
        marketString += ("Todays price of "+traded_stocks[i].name+" is "+str(traded_stocks[i].current_price)+"\n")
    print("\nDay "+str(t)+".\n"+marketString)

    print("Accounts on market:")
    print(accList)

    #get and check name
    name = input("\nWho will trade? (press enter to go to next day)")
    if name != "":
        index_Acc=getAccount(name, accList)
        while index_Acc is None:
            print("Name not found, try again.")
            name = input("Who will trade?")
            index_Acc = getAccount(name, accList)

        buyOrSell = input("\nBuy or sell?").upper()
        while buyOrSell not in ("BUY", "SELL"):
            print("Not a valid option, try again:")
            buyOrSell = input("Buy or sell?").upper()

        #get and check ticker
        print("\nStocks on market: ")
        print(traded_stocks)
        ticker=input("Which Ticker?").upper()
        index_Stock=getStockIndex(ticker, traded_tickers)
        while index_Stock is None:
            print("Not a valid ticker, try again:")
            ticker = input("Which Ticker?").upper()
            index_Stock = getStockIndex(ticker, traded_tickers)

        #get and check quantity
        validQuant = False
        while not validQuant:
            try:
                quant = int(input("How many stocks?"))
                if quant <= 0:
                    print("You only trade in positives, try again:")
                else:
                    validQuant = True
            except:
                print("Not a valid number, try again:")

        accList[index_Acc].makeTransaction(traded_stocks[index_Stock], quant, buyOrSell)
        accList[index_Acc].printPortfolio(traded_stocks, traded_tickers)

        play = input("\nKeep playing? Y/N").upper()
        if play != 'Y':
            cont = False
    #this else is if you just want to go through time
    else:
        print("\n")
        for i in range (0,len(accList)):
            accList[i].printPortfolio(traded_stocks, traded_tickers)
    t += 1

print("Thanks for playing with us!")