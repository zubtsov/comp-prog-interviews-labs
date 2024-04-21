from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        if l <= 1:
            return

        left_shift = 0

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                left_shift += 1
            else:
                nums[i - left_shift] = nums[i]
            i += 1

        i = -left_shift
        while i < 0:
            nums[i] = 0
            i += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
