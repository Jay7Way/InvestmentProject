class Order:
    volume = 0
    ticker = ""
    timeStamp = ""
    value = 0
    Account = ""

    def __init__(self, inputTicker, inputVolume, inputValue):
        self.volume = inputVolume
        self.ticker = inputTicker
        self.value = inputValue
        self.direction = 1

    def totalCost(order):
        if order:
            print(order.direction * order.volume * order.value)
            return order.direction * order.volume * order.value
        else:
            return 0

class Buy(Order):
    def __init__(self, inputTicker, inputVolume, inputValue):
        Order.__init__(self, inputTicker, inputVolume, inputValue)
        self.direction = -1


class Sell(Order):
    def __init__(self, inputTicker, inputVolume, inputValue):
        Order.__init__(self, inputTicker, inputVolume, inputValue)
        self.direction = 1



