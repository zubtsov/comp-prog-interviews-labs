from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2[:]
            return
        if nums2[0] >= nums1[m - 1]:
            nums1[-n:] = nums2
            return

        index_m = m - 1
        index_n = n - 1
        while index_m >= 0 or index_n >= 0:
            index_mn = index_m + index_n + 1
            if index_m < 0:
                nums1[index_mn] = nums2[index_n]
                index_n -= 1
            elif index_n < 0:
                nums1[index_mn] = nums1[index_m]
                index_m -= 1
            elif nums1[index_m] >= nums2[index_n]:
                nums1[index_mn] = nums1[index_m]
                index_m -= 1
            else:
                nums1[index_mn] = nums2[index_n]
                index_n -= 1


if __name__ == '__main__':
    l1 = [1, 0, 0, 0, 0, 0]
    l2 = [2, 3, 4, 5, 6]
    Solution().merge(l1, 1, l2, 5)
    print(l1)
