import threading
import webbrowser

from flask import Flask, request, render_template
#from .main import traded_stocks
from .Functions.AccountsCreator import accountsCreator
from .Functions.DataParser import dataParser
from .Functions.MainFunctions import getAccount, getStockIndex
from .Stock import Stock

app = Flask(__name__)

global stock
global buyOrSell
global amount
global loggedin_user

traded_tickers=["AAPL", "GOOGL"] #temp small set

accList, df = accountsCreator(True)

traded_stocks=""

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        loggedin_user=request.hello["username"]
        index_Acc = getAccount(loggedin_user, accList)
        while index_Acc is None:
            print("Name not found, try again.")
            loggedin_user=request.hello["username"]
            index_Acc = getAccount(loggedin_user, accList)
        AAPL_history = dataParser("AAPL", "history")
        GOOGL_history = dataParser("GOOGL", "history")

        apple = Stock(AAPL_history[-1], "Apple", "AAPL", AAPL_history)
        google = Stock(GOOGL_history[-1], "Google", "GOOGL", GOOGL_history)
        global traded_stocks
        traded_stocks = [apple, google]
        marketString = ""
        for i in range(0, len(traded_stocks)):
            traded_stocks[i].update_price(1)
            marketString += ("Todays price of " + traded_stocks[i].name + " is " + str(
                traded_stocks[i].current_price) + ". ")

        password = request.hello["password"]
        if password == "guest":
            return render_template("form.html", marketString=marketString)
        else:
            return render_template("hello.html")
    else:
        return render_template("hello.html")



@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        stock = request.form["stock"]
        if stock == "error1":
            return render_template("form.html")
        else:
            amount = request.form["amount"]
            buyOrSell = request.form["buyorsell"]
            if buyOrSell == "error2":
                return render_template("form.html")
            else:
                i = getStockIndex(traded_stocks, stock)
                price = traded_stocks[i]
                costs = (int(amount)*price)
                return "You have bought " + amount + " of " + stock + ", at a price of " + str(price) + "; which costs: €" + str(costs)
    else:
        return render_template("form.html")



