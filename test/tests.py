import unittest

from Order import Buy, Sell
from Stock import Stock


class TestCases(unittest.TestCase):
    def test_buy(self):
        order1 = Buy("GOOGL", 1000, 10)
        self.assertEqual(Buy.totalCost(order1), -10000)

    def test_sell(self):
        order2 = Sell("AAPL", 50, 30)
        self.assertEqual(Buy.totalCost(order2), 1500)

    def testPriceCheck(self):
        price = Stock.getprice("AAPL")
        self.assertEqual(10, price)

if __name__ == '__main__':
    unittest.main()