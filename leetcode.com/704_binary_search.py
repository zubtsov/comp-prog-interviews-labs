from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        middle_index = (right_index + left_index) // 2

        while left_index < right_index:
            current = nums[middle_index]
            if current < target:
                left_index = middle_index + 1
            elif current > target:
                right_index = middle_index - 1
            elif current == target:
                return middle_index
            middle_index = (right_index + left_index) // 2

        if nums[middle_index] == target:
            return middle_index

        return -1


if __name__ == '__main__':
    nums = [2, 5]
    target = 5
    print(Solution().search(nums, target))
