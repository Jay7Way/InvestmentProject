import unittest

from Classes.Order import Buy, Sell, totalCost


class TestCases(unittest.TestCase):
    def test_buy(self):
        order1 = Buy("GOOGL", 1000, 10)
        self.assertEqual(totalCost(order1), -10000)

    def test_sell(self):
        order2 = Sell("AAPL", 50, 30)
        self.assertEqual(totalCost(order2), 1500)


if __name__ == '__main__':
    unittest.main()