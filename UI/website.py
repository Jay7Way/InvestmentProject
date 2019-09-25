from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html")

db = {'GOOGL':5,'MFST':6,'AAPL':5}



@app.route('/stock')
def stock():
    return render_template("stock.html",
                           db=db)

@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == "POST":
        stock = request.form["stock"]
        amount = request.form["amount"]
        price = db[stock]
        costs = (int(amount)*price)
        if stock == "error1":
            exit()


        return "You have bought " + amount + " of " + stock + ", which costs: " + str(costs)
    else:
        return render_template("form.html")
