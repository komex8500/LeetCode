# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = [head]
        cur = head
        while cur.next:
            l.append(cur)
            cur = cur.next
        l.append(cur)
        if len(l) % 2 == 0:
            return l[len(l)//2]
        else:
            return l[(len(l)//2)+1]
            