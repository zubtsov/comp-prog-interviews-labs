class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_sum_of_squares(self, n):
        return sum([i * i for i in range(1, n + 1)])

    def level_2_sum_of_squares(self, m, n):
        return sum([i * i for i in range(m, n + 1)])
