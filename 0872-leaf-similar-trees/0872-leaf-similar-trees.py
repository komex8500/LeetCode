# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafValueSequence(root) -> List[int]:
            result = []
            st = []
            if root:
                st.append(root)
            while st:
                cur = st.pop()
                if cur != None:
                    if cur.right == None and cur.left == None:
                        result.append(cur.val)
                        continue
                    if cur.right:
                        st.append(cur.right)
                    if cur.left:
                        st.append(cur.left)
            return result

        r1 = getLeafValueSequence(root1)
        r2 = getLeafValueSequence(root2)
        return r1 == r2