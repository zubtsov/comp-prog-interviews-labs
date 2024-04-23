from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        majority_number = None
        counter = 0
        i = 0
        while i <= len(nums) - counter:
            n = nums[i]

            if majority_number == n:
                counter += 1
            elif counter > 0:
                counter -= 1
            else:
                majority_number = n
                counter = 1
            i += 1

        return majority_number
