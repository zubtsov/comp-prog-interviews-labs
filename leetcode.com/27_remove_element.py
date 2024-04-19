from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return len(nums)

        current_index = 0
        index_to_borrow_element = len(nums) - 1
        num_elems_eq_val = 0

        while current_index <= index_to_borrow_element:
            if nums[current_index] == val:
                num_elems_eq_val += 1
                while nums[index_to_borrow_element] == val and index_to_borrow_element > current_index:
                    index_to_borrow_element -= 1
                    num_elems_eq_val += 1

                if index_to_borrow_element > current_index:
                    nums[current_index] = nums[index_to_borrow_element]
                index_to_borrow_element -= 1
            current_index += 1

        if num_elems_eq_val > 0:
            nums[-num_elems_eq_val:] = []
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [4,5]
    k = s.removeElement(nums, 5)
    print(k)
    print(nums)
