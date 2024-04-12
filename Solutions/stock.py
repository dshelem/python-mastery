"""
stock.py
# (c) Denis Shelemekh, 2023-2024
"""
import csv


class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n


# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            s = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(s)
    return portfolio


def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(f'{"-"*10} {"-"*10} {"-"*10}')
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
