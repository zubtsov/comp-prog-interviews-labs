from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_min_and_move(self, cn1: Optional[ListNode], cn2: Optional[ListNode]) -> (ListNode, ListNode, ListNode):
        cn1next = cn1
        cn2next = cn2

        if not cn2:
            min_node = cn1
            cn1next = cn1.next
        elif not cn1:
            min_node = cn2
            cn2next = cn2.next
        elif cn1.val <= cn2.val:
            min_node = cn1
            cn1next = cn1.next
        elif cn1.val > cn2.val:
            min_node = cn2
            cn2next = cn2.next

        return min_node, cn1next, cn2next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        current_node1 = list1
        current_node2 = list2

        first_node, current_node1, current_node2 = self.get_min_and_move(current_node1, current_node2)
        current_node = first_node

        while current_node1 or current_node2:
            new_node, current_node1, current_node2 = self.get_min_and_move(current_node1, current_node2)
            current_node.next = new_node
            current_node = new_node

        return first_node
