class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_find_list_1_in_list_2(self, list_1, list_2):
        for i in range(len(list_2) - len(list_1) + 1):
            for j in range(len(list_1)):
                if list_1[j] != list_2[i + j]:
                    break
            else:
                return i
        return -1

    def level_2_longest_common_stretch(self, list_1, list_2):
        list_1_start = 0
        list_2_start = 0
        longest_common_stretch_length = 0

        for i in range(len(list_1)):
            for j in range(len(list_2)):
                current_list_1_start = -1
                current_list_2_start = -1
                current_common_stretch_length = 0

                max_k = min(len(list_1) - i, len(list_2) - j)
                for k in range(max_k):
                    if list_1[i + k] == list_2[j + k]:
                        if current_list_1_start == -1:
                            current_list_1_start = i + k
                        if current_list_2_start == -1:
                            current_list_2_start = j + k
                        current_common_stretch_length += 1
                    if list_1[i + k] != list_2[j + k] or k == max_k - 1:
                        if longest_common_stretch_length < current_common_stretch_length:
                            longest_common_stretch_length = current_common_stretch_length
                            list_1_start = current_list_1_start
                            list_2_start = current_list_2_start
                        current_common_stretch_length = 0
                        current_list_1_start = -1
                        current_list_2_start = -1

        return [longest_common_stretch_length, list_1_start, list_2_start]
