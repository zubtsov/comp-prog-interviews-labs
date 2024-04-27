from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left_half_head = None
        right_half_head = head
        end_indicator = head

        while end_indicator and end_indicator.next:
            end_indicator = end_indicator.next.next

            tmp = right_half_head.next
            right_half_head.next = left_half_head
            left_half_head = right_half_head
            right_half_head = tmp

        if end_indicator and not end_indicator.next:
            # right_half_head is in the center, the number of elements is odd
            right_half_head = right_half_head.next

        while left_half_head or right_half_head:
            if left_half_head.val != right_half_head.val:
                return False
            left_half_head = left_half_head.next
            right_half_head = right_half_head.next

        return True


if __name__ == '__main__':
    vals = [1, 2, 2, 1]
    head = ListNode(vals[0])
    current = head
    for i in range(1, len(vals)):
        current.next = ListNode(vals[i])
        current = current.next

    print(Solution().isPalindrome(head))
