"""
pcost.py
# (c) Denis Shelemekh, 2023
"""


def portfolio_cost(filepath: str) -> float:
    pcost = 0.0
    with open(f'../{filepath}', 'r') as f:
        while string := f.readline()[:-1]:
            _, shares, price = string.split()
            shown_string = False
            # print(shares, price)
            try:
                shares = int(shares)
            except Exception as e:
                if not shown_string:
                    print(f'Couldn\'t parse \'{string}\'')
                shown_string = True
                print(f'Reason: {e}')
                shares = 0
            try:
                price = float(price)
            except Exception as e:
                if not shown_string:
                    print(f'Couldn\'t parse \'{string}\'')
                shown_string = True
                print(f'Reason: {e}')
                price = 0.0
            pcost += int(shares) * float(price)
            shown_string = False
    return round(pcost, 2)


if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))
