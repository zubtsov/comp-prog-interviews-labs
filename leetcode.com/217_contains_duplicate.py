from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        already_seen_values = set()

        i = 0
        while i < len(nums):
            elem = nums[i]
            if elem in already_seen_values:
                return True
            else:
                already_seen_values.add(elem)
            i += 1
        return False
