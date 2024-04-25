import sys
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head
        turtle_moves = False

        while rabbit is not None:
            rabbit = rabbit.next
            if rabbit == turtle:
                return True
            if turtle_moves:
                turtle = turtle.next
                turtle_moves = False
            else:
                turtle_moves = True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        while head:
            if sys.getrefcount(head) > 3:
                return True
            head = head.next
        return False
