"""
# readrides_tuples.py
# (c) Denis Shelemekh, 2023
"""
import csv

"""
# A tuple
row = (route, date, daytype, rides)

# A dictionary
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}



# A named tuple
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# A class with __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
        
"""


# A class with __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class_wit_slots(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_class_wit_slots('../Data/ctabus.csv')
    print('-= Read as classes with slots =-')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
