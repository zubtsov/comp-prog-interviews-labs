class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_consecutive_check(self, int_list):
        int_list.sort()
        if abs(int_list[-1] - int_list[0]) == len(int_list) - 1:
            return int_list
        else:
            return []

    def level_2_missing_numbers(self, int_list):
        int_list.sort()
        missing_numbers = []
        for i in range(1, len(int_list)):
            for j in range(int_list[i - 1] + 1, int_list[i]):
                missing_numbers.append(j)
        return missing_numbers
