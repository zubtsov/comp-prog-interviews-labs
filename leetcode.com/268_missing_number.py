from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sum_of_arithmetic_progression = l * (l + 1) / 2
        real_sum = sum(nums)
        return int(sum_of_arithmetic_progression - real_sum)


if __name__ == '__main__':
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums))
