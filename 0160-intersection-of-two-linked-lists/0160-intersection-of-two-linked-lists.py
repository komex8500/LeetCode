# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        prevA = ListNode(next=headA)
        prevB = ListNode(next=headB)
        curA = prevA.next
        curB = prevB.next
        size = 0
        while curA and curB:
            curA = curA.next
            curB = curB.next
        if curB:
            prevA, prevB = prevB, prevA
            curA, curB = curB, curA
        while curA:
            curA = curA.next
            size += 1
        curA = prevA.next
        curB = prevB.next
        for _ in range(size):
            curA = curA.next
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None