import threading
import webbrowser

from flask import Flask, request, render_template

app = Flask(__name__)
url = "http://127.0.0.1:5000"
threading.Timer(5, lambda: webbrowser.open(url)).start()

@app.route('/',methods=['POST','GET'])
def hello():
    if request.method == "POST":
        username=request.form["username"]
        password = ""
        while password != "guest":
            password = request.form["password"]
            if password != "guest":
                print("incorrect password")
    return render_template("hello.html")

db = {'GOOGL':5.4,'MFST':6,'AAPL':5, 'INIC':70}

@app.route('/stock')
def stock():
    return render_template("stock.html",
                           db=db)

@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == "POST":
        stock = request.form["stock"]
        if stock == "error1":
            return render_template("form.html")
        else:
            amount = request.form["amount"]
            price = db[stock]
            costs = (int(amount)*price)
            return "You have bought " + amount + " of " + stock + ", at a price of " + str(price) + "; which costs: €" + str(costs)
    else:
        return render_template("form.html")
