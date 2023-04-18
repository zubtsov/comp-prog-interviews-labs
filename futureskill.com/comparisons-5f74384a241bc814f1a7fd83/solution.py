class Solution:
    def __init__(self, api):
        self.api = api

    def is_equal(self, a, b):
        return a == b

    def is_not_equal(self, a, b):
        return a != b

    def is_less(self, a, b):
        return a < b

    def is_less_or_equal(self, a, b):
        return a <= b

    def is_greater(self, a, b):
        return a > b

    def is_greater_or_equal(self, a, b):
        return a >= b