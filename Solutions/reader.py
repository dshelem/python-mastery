"""
reader.py
# (c) Denis Shelemekh, 2023
"""
import csv
import collections


# A function that reads a csv file into a list of dicts
def read_csv_as_dicts(filename, coltypes):
    data = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
            data.append(record)
    return data


class DataCollection(collections.abc.Sequence):
    def __init__(self, headers, coltypes):
        self.data = []
        self.headers = headers
        self.coltypes = coltypes
        self.columns_no = len(headers)
        for i in range(self.columns_no):
            # Columns
            self.data.append([])

    def __len__(self):
        # all lists assume to be the same length
        if self.columns_no:
            return len(self.data[0])
        return RuntimeError

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
                row = []
                for col_no in self.columns_no:
                    row.append(self.data[col_no][i])
                record = {name: val for name, val in zip(self.headers, row)}
                ret_values.append(record)

            return ret_values

        row = []
        for col_no in range(self.columns_no):
            row.append(self.data[col_no][item])
        return {name: val for name, val in zip(self.headers, row)}

    def append(self, d):
        for col_no in range(self.columns_no):
            self.data[col_no].append(self.coltypes[col_no](d[col_no]))


def read_csv_as_columns(filename, coltypes):
    '''
    Read the bus ride data into DataCollection
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Get headers
        data = DataCollection(headings, coltypes)
        for row in rows:
            data.append(row)
    return data
