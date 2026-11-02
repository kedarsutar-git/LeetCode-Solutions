# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        q = []
        res = []
        current_level = 0
        q.append(root)

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len(q)):
                node = q.pop(0)
                res[current_level].append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            current_level += 1

        return res

               

        