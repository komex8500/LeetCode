# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            cur_p = stack_p.pop()
            cur_q = stack_q.pop()
            if cur_p == None and cur_q == None:
                continue
            if not cur_p or not cur_q:
                return False
            if cur_p.val != cur_q.val:
                return False
            stack_p.append(cur_p.left)
            stack_q.append(cur_q.left)
            stack_p.append(cur_p.right)
            stack_q.append(cur_q.right)
        return not stack_p and not stack_q
        