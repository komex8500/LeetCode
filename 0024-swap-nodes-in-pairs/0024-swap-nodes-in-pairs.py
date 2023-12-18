# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(next=head)
        cur = prev
        while cur.next and cur.next.next:
            tmp = cur.next
            next = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = tmp
            tmp.next = next
            cur = tmp
        return prev.next