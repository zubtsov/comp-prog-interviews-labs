class Solution:
    def __init__(self, api):
        self.api = api

    def selection_sort(self, list_var):
        for i in range(len(list_var)):
            next_smallest_number_idx = i
            for j in range(i + 1, len(list_var)):
                if list_var[j] < list_var[next_smallest_number_idx]:
                    next_smallest_number_idx = j

            if next_smallest_number_idx != i:
                list_var[i], list_var[next_smallest_number_idx] = list_var[next_smallest_number_idx], list_var[i]

        return list_var

    def insertion_sort(self, list_var):
        for i in range(1, len(list_var)):
            if list_var[i] >= list_var[i - 1]:
                continue

            for j in range(i - 1, -1, -1):
                if list_var[i] >= list_var[j]:
                    list_var.insert(j + 1, list_var[i])
                    del list_var[i + 1]
                    break
            else:
                list_var.insert(0, list_var[i])
                del list_var[i + 1]

        return list_var

    def bubble_sort(self, list_var):
        swapped_elements = True

        while swapped_elements:
            swapped_elements = False
            for i in range(len(list_var) - 1):
                if list_var[i] > list_var[i + 1]:
                    list_var[i], list_var[i + 1] = list_var[i + 1], list_var[i]
                    swapped_elements = True

        return list_var

    def merge_sort(self, list_var):
        if len(list_var) <= 1:
            return list_var
        elif len(list_var) == 2:
            if list_var[0] <= list_var[1]:
                return list_var
            else:
                return list_var[::-1]

        middle_index = len(list_var) // 2
        left_half = self.merge_sort(list_var[:middle_index])
        right_half = self.merge_sort(list_var[middle_index:])

        left_index = 0;
        right_index = 0;
        result = []
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                result.append(left_half[left_index])
                left_index += 1
            else:
                result.append(right_half[right_index])
                right_index += 1

        if right_index < len(right_half):
            result += right_half[right_index:]
        else:
            result += left_half[left_index:]

        return result

    @staticmethod
    def swap_elements(l, i, j):
        if i == j:
            return
        l[i], l[j] = l[j], l[i]

    @staticmethod
    def quicksort2(list_var, first_index, last_index):
        if last_index - first_index + 1 <= 1:
            return list_var
        elif last_index - first_index + 1 == 2:
            if list_var[first_index] > list_var[last_index]:
                Solution.swap_elements(list_var, first_index, last_index)
            return list_var
        else:
            middle_index = (first_index + last_index) // 2
            min_elem = min(list_var[first_index], list_var[middle_index], list_var[last_index])
            max_elem = max(list_var[first_index], list_var[middle_index], list_var[last_index])
            if min_elem <= list_var[middle_index] <= max_elem:
                Solution.swap_elements(list_var, middle_index, last_index)
            elif min_elem <= list_var[first_index] <= max_elem:
                Solution.swap_elements(list_var, first_index, last_index)
            # now the pivot element is at the last index
            i, j = first_index, last_index - 1
            while i < j:
                while list_var[i] < list_var[last_index]:
                    i += 1
                while list_var[j] >= list_var[last_index] and i < j:
                    j -= 1
                if i < j:
                    Solution.swap_elements(list_var, i, j)
            Solution.swap_elements(list_var, i, last_index)
            # now the pivot element is where it should be in the sorted array
            Solution.quicksort2(list_var, first_index, i - 1)
            Solution.quicksort2(list_var, i + 1, last_index)
            return list_var

    def quicksort(self, list_var):
        Solution.quicksort2(list_var, 0, len(list_var) - 1)
        return list_var
