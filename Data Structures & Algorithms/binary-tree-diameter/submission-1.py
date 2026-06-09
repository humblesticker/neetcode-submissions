# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxd = 0

    def walk(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        ld = self.walk(root.left)
        rd = self.walk(root.right)
        self.maxd = max(self.maxd, ld + rd)
        return 1 + max(ld, rd)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.walk(root)
        return self.maxd
        
"""
extra varaible?
extra
"""