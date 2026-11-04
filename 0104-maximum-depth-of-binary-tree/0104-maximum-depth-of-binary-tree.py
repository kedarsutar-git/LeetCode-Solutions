# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0 

        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)

        return max(leftdepth,rightdepth) + 1