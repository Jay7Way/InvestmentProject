class MarketOperator:
    value = 0

    def __init__(self, initialValue):
        self.value = initialValue

    def profit(self, margin):
        self.value += margin
        print("New profit for the operator is: " + str(margin) + "\n"
         "Total earnings by the operator are:  " + str(self.value), "\n \n")


operator = MarketOperator(1000)

print(operator.value)

operator.profit(100)


