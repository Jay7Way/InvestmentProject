import threading
import webbrowser

from flask import Flask, request, render_template

app = Flask(__name__)
url = "http://127.0.0.1:5000"
threading.Timer(5, lambda: webbrowser.open(url)).start()


@app.route('/', methods=['POST','GET'])
def hello():
    password = ""
    if request.method == "POST":
        global loggedin_user
        loggedin_user=request.hello["username"]
<<<<<<< HEAD
        while password != "guest":
            password = request.hello["password"]
            if password == "guest":
                return render_template("form.html")
=======
        password = request.hello["password"]
        if password == "guest":
            return render_template("form.html")
        else:
            return render_template("hello.html")
>>>>>>> 1b89403ffccc01622207b6d80fcab25c9f1711cd
    else:
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
