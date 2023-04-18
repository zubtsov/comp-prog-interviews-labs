class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_index_for_max_product(self, integer_list):
        max_product = integer_list[0] * integer_list[1]
        max_product_index = 0
        for i in range(1, len(integer_list) - 1):
            current_product = integer_list[i] * integer_list[i + 1]
            if current_product > max_product:
                max_product = current_product
                max_product_index = i
        return max_product_index

    def level_2_index_for_max_product(self, integer_list, n):
        max_product = integer_list[0]
        for i in range(1, n):
            max_product *= integer_list[i]

        max_product_index = 0
        for i in range(0, len(integer_list) - n):
            current_product = integer_list[i]
            for j in range(i + 1, i + n):
                current_product *= integer_list[j]

            if current_product > max_product:
                max_product = current_product
                max_product_index = i
        return max_product_index
