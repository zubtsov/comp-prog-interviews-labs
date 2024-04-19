from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        while index < len(nums) and nums[index] < target:
            index += 1
        return index