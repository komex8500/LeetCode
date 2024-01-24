# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.result = 0
        count = [0] * 10
        self.search(root, count)
        return self.result

    def search(self, root, count):
        if not root:
            return
        count[root.val] += 1
        self.search(root.left, count)
        self.search(root.right, count)
        if not root.left and not root.right:
            self.check(count)
        count[root.val] -= 1

    def check(self, count):
        odd = 0
        for i in range(1, 10):
            if count[i] % 2 != 0:
                odd += 1
            if odd > 1:
                break
        if odd <= 1:
            self.result += 1