from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)

        last_unique_index = 0
        current_index = 1

        while current_index < len(nums):
            if nums[last_unique_index] != nums[current_index]:
                last_unique_index += 1
                nums[last_unique_index] = nums[current_index]
            current_index += 1

        num_elements_to_remove = (len(nums) - last_unique_index - 1)

        if num_elements_to_remove > 0:
            nums[-num_elements_to_remove:] = []

        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    print(s.removeDuplicates(nums))
    print(nums)
