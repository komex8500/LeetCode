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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(next=head)
        fast = prev
        cur = prev
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            cur = cur.next
        cur.next = cur.next.next
        return prev.next