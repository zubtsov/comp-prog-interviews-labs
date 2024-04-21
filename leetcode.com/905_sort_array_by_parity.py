from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left_i = 0
        right_i = len(nums) - 1

        while left_i < right_i:
            if nums[left_i] % 2 == 0:
                left_i += 1
            elif nums[right_i] % 2 == 1:
                right_i -= 1
            else:
                nums[left_i], nums[right_i] = nums[right_i], nums[left_i]
                left_i += 1
                right_i -= 1
        return nums
