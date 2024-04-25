import sys
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen_nodes_a = set()
        seen_nodes_b = set()

        while headA or headB:
            if headA:
                if headA in seen_nodes_b:
                    return headA
                seen_nodes_a.add(headA)
                headA = headA.next
            if headB:
                if headB in seen_nodes_a:
                    return headB
                seen_nodes_b.add(headB)
                headB = headB.next

        return None

    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA:
            if sys.getrefcount(headA) > 3:
                return headA
            headA = headA.next
        while headB:
            if sys.getrefcount(headB) > 3:
                return headB
            headB = headB.next
        return None
