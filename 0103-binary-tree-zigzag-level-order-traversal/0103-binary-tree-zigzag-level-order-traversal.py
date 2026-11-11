# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [[root.val]]


        q = []
        res = []
        q.append(root)

        left_to_right = True 

        while q:
            len_q = len(q)
            row = [0]*len_q

            for i in range(len_q):
                node = q.pop(0)

                if left_to_right:
                    index = i

                else:
                    index = len_q - 1 - i

                row[index] = node.val

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            res.append(row)

            if left_to_right:
                left_to_right = False

            else:
                left_to_right = True

        return res



        