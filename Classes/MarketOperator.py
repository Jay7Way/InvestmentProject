class MarketOperator:
    value = 0

    def profit(self, margin):
        self.value += margin
        print("New profit for the operator is: " + str(margin) + "\n"
         "Total earnings by the operator are:  " + str(self.value), "\n \n")


operator = MarketOperator()

print(operator.value)


operator.profit(100)
operator.profit(1000)
operator.profit(10000)


