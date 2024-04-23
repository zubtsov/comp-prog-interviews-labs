from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counts = [0] * 1001

        for n in nums1:
            nums1_counts[n] += 1

        res = []

        for n in nums2:
            if nums1_counts[n] > 0:
                res.append(n)
                nums1_counts[n] -= 1

        return res
