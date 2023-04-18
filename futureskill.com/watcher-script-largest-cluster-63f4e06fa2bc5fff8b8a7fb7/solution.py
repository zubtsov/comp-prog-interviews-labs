class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_most_common_number(self, int_list):
        numbers_counts = {}

        for i in int_list:
            if i in numbers_counts:
                numbers_counts[i] += 1
            else:
                numbers_counts[i] = 1

        most_common_number = None
        most_common_number_count = 0

        for n, c in numbers_counts.items():
            if c > most_common_number_count:
                most_common_number = n
                most_common_number_count = c

        return most_common_number

    def level_2_largest_cluster(self, int_list):
        largest_cluster_start = 0
        largest_cluster_length = 1

        current_cluster_start = 0
        current_cluster_length = 1

        for i in range(1, len(int_list)):
            if int_list[i] == int_list[current_cluster_start]:
                current_cluster_length = i - current_cluster_start + 1
            else:
                if current_cluster_length > largest_cluster_length:
                    largest_cluster_length = current_cluster_length
                    largest_cluster_start = current_cluster_start
                current_cluster_start = i
                current_cluster_length = 1

        return largest_cluster_start
