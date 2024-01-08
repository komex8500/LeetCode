# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        stack = []
        cur = root
        while cur or stack:
            if cur:
                if cur.val < low:
                    cur = cur.right
                else:
                    stack.append(cur)
                    cur = cur.left
            else:
                cur = stack.pop()
                if cur.val > high:
                    break
                if cur.val >= low and cur.val <= high:
                    result += cur.val
                cur = cur.right
        return result