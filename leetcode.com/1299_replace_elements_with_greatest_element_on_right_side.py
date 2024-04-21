from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right_elem = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for i in reversed(range(len(arr) - 1)):
            max_right_elem_candidate = arr[i]
            arr[i] = max_right_elem
            if max_right_elem_candidate > max_right_elem:
                max_right_elem = max_right_elem_candidate

        return arr
