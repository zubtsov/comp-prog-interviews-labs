from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None

        while head:
            next_element = head.next
            head.next = previous
            previous = head
            head = next_element

        return previous

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListRecursively(prev, current):
            if current:
                next_element = current.next
                current.next = prev
                return reverseListRecursively(current, next_element)
            else:
                return prev

        return reverseListRecursively(None, head)


if __name__ == '__main__':
    head = ListNode()
    current = head
    for i in range(1, 5):
        current.next = ListNode(i)
        current = current.next

    reversed_list = Solution().reverseList2(head)
    print('done')
