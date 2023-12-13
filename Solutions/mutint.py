"""
mutint.py
# (c) Denis Shelemekh, 2023
"""

from functools import total_ordering


@total_ordering
class MutInt:

    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __format__(self, format_spec):
        return format(self.value, format_spec)

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        if isinstance(other, int):
            return MutInt(self.value + other)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value - other.value)
        if isinstance(other, int):
            return MutInt(self.value - other)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, MutInt):
            return MutInt(other.value - self.value)
        if isinstance(other, int):
            return MutInt(other - self.value)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        if isinstance(other, int):
            self.value += other
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, MutInt):
            self.value -= other.value
            return self
        if isinstance(other, int):
            self.value -= other
            return self
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return NotImplemented

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    __index__ = __int__
