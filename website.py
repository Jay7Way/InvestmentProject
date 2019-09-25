from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
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
            exit()
        else:
            amount = request.form["amount"]
            price = db[stock]
            costs = (int(amount)*price)
            return "You have bought " + amount + " of " + stock + ", at a price of " + str(price) + "; which costs: €" + str(costs)
    else:
        return render_template("form.html")
