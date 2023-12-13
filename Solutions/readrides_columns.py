"""
readrides_columns.py
# (c) Denis Shelemekh, 2023
"""
import csv
import collections


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # all lists assume to be the same length
        return len(self.routes)

    def __getitem__(self, item):
        if isinstance(item, slice):
            ret_values = []

            start = 0 if item.start is None else item.start
            stop = len(self) if item.stop is None else item.stop
            if item.step is None:
                step = -1 if stop < start else 1
            else:
                step = item.step

            for i in range(start, stop, step):
                val = {
                    'route': self.routes[i],
                    'date': self.dates[i],
                    'daytype': self.daytypes[i],
                    'rides': self.numrides[i],
                }
                ret_values.append(val)

            return ret_values

        return {
            'route': self.routes[item],
            'date': self.dates[item],
            'daytype': self.daytypes[item],
            'rides': self.numrides[item],
        }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records