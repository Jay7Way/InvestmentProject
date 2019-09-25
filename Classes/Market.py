class Market(object):

    def __init__(self, bids, asks):
        self.bids = bids
        self.asks = asks
        self.accounts = []

    def AddAccount(self, name, id, balance, portfolio, orders):
        self.accounts.append([name, id, balance, portfolio, orders])