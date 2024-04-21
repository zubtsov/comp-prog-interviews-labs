from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        left_index = 0
        right_index = len(arr) - 1

        while left_index < len(arr) - 1:
            if arr[left_index] < arr[left_index + 1]:
                left_index += 1
            elif arr[left_index] > arr[left_index + 1]:
                break
            else:
                return False

        while right_index > left_index:
            if arr[right_index] < arr[right_index - 1]:
                right_index -= 1
            elif arr[right_index] > arr[right_index - 1]:
                break
            else:
                return False

        return left_index == right_index and left_index != 0 and right_index != len(arr) - 1
