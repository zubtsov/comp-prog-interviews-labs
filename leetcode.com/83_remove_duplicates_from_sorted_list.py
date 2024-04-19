from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        last_unique_node = head
        current_node = head.next

        while current_node:
            while current_node and last_unique_node.val == current_node.val:
                current_node = current_node.next
            last_unique_node.next = current_node
            last_unique_node = current_node
            if current_node:
                current_node = current_node.next

        return head
