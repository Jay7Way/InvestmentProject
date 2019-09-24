class Order:
    volume = 0
    timeStamp = ""
    value = 0
    Account = ""

    def __init__(self, inputVolume, inputTimeStamp, inputValue):
        self.volume = inputVolume
        self.timeStamp = inputTimeStamp
        self.value = inputValue
        self.direction = 0


class Buy(Order):
    def __init__(self, inputVolume, inputTimeStamp, inputValue):
        Order.__init__(self, inputVolume, inputTimeStamp, inputValue)
        self.volume = inputVolume
        self.timeStamp = inputTimeStamp
        self.value = inputValue
        self.direction = -1


class Sell(Order):
    def __init__(self, inputVolume, inputTimeStamp, inputValue):
        Order.__init__(self, inputVolume, inputTimeStamp, inputValue)
        self.volume = inputVolume
        self.timeStamp = inputTimeStamp
        self.value = inputValue
        self.direction = 1


def totalCost(order):
    print(order.direction * order.volume * order.value)
    return order.direction * order.volume * order.value


order1 = Buy(100, "", 20)
totalCost(order1)

order2 = Sell(100, "", 20)
totalCost(order2)

