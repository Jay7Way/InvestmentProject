class Order:
    volume = 0
    timeStamp = ""
    value = 0

    def __init__(self, inputVolume, inputTimeStamp, inputValue):
        self.volume = inputVolume
        self.timeStamp = inputTimeStamp
        self.value = inputValue

order = Order(100, 10/10/2010, 100)


class Buy(Order):
    def __init__(self, inputVolume, inputTimeStamp, inputValue):
        Order.__init__(inputVolume, inputTimeStamp, inputValue)
        self.volume = inputVolume
        self.timeStamp = inputTimeStamp
        self.value = inputValue


class Sell(Order):
    def __init__(self, inputVolume, inputTimeStamp, inputValue):
        Order.__init__(inputVolume, inputTimeStamp, inputValue)
        self.volume = inputVolume
        self.timeStamp = inputTimeStamp
        self.value = inputValue


def totalCost(order):
    print(order.volume*order.Value)
    return order.volume*order.Value




