# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.Max = float("-inf")

        def MaxPathDown(node):
            if node is None:
                return 0

            leftsum = max(0, MaxPathDown(node.left))
            rightsum = max(0, MaxPathDown(node.right))

            self.Max = max(self.Max,leftsum + rightsum + node.val)

            return node.val + max(leftsum, rightsum)

        MaxPathDown(root)

        return self.Max
