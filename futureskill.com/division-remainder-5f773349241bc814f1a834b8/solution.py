class Solution:
    def __init__(self, api):
        self.api = api

    def compare_remainder(self, a, b):
        if a % 5 > b % 5:
            return a
        elif a % 5 < b % 5:
            return b
        return 0
