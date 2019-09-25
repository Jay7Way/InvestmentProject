class Order:
    volume = 0
    ticker = ""
    timeStamp = ""
    value = 0
    Account = ""

    def __init__(self, inputTicker,inputVolume, inputTimeStamp, inputValue):
        self.volume = inputVolume
        self.ticker = inputTicker
        self.timeStamp = inputTimeStamp
        self.value = inputValue
        self.direction = 0


class Buy(Order):
    def __init__(self, inputTicker, inputVolume, inputTimeStamp, inputValue):
        Order.__init__(self, inputTicker, inputVolume, inputTimeStamp, inputValue)
        self.direction = -1


class Sell(Order):
    def __init__(self, inputTicker, inputVolume, inputTimeStamp, inputValue):
        Order.__init__(self, inputTicker, inputVolume, inputTimeStamp, inputValue)
        self.direction = 1


def totalCost(order):
    print(order.direction * order.volume * order.value)
    return order.direction * order.volume * order.value


order1 = Buy("GOOGL",1000, "", 10)


totalCost(order1)

order2 = Sell("AAPL", 50, "", 30)

totalCost(order2)

