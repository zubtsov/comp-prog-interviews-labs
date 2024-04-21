from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        left_i = 0
        right_i = len(nums) - 1

        while left_i <= right_i:
            index = right_i - left_i

            left_s = nums[left_i] * nums[left_i]
            right_s = nums[right_i] * nums[right_i]

            if left_s > right_s:
                res[index] = left_s
                left_i += 1
            else:
                res[index] = right_s
                right_i -= 1

        return res


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))
