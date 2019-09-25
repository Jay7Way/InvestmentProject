def getAccount(accName, accList):
    for i in range (0,len(accList)):
        if accList[i].name == accName:
            return i
    return None

def getStock(stockName, stockList):
    for i in range (0,len(stockList)):
        if stockList[i] == stockName:
            return i
    return None

# TO BUILD
def BuyStock(account, stock, quantity):
    price = stock.get_current_price()
    if account.balance > price*quantity:
        account.balance += self.balance + Buy.totalCost(Buy(ticker, quantity, price))
        account.AddStock(ticker, quantity)
    else:
        Exception("Insufficient funds in the account to process this purchase")