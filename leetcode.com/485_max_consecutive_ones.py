from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cco = 0
        mco = 0
        i = 0

        while i < len(nums):
            if nums[i] == 1:
                cco += 1
            else:
                if cco > mco:
                    mco = cco
                cco = 0
            i += 1
        return max(cco, mco)
