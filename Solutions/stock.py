"""
stock.py
# (c) Denis Shelemekh, 2023
"""


class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
