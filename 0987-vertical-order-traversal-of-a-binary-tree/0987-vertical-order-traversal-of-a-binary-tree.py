# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,node,row,column,nodes):
        if node is None:
            return 

        nodes.append((column, row, node.val))

        self.DFS(node.left,row+1, column-1, nodes)

        self.DFS(node.right,row+1,column+1,nodes)

    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        nodes = []

        self.DFS(root,0,0,nodes)

        nodes.sort()
        ans = []

        pre_column = None

        for column, row, val in nodes:
            if pre_column is None or column != pre_column:
                ans.append([])
                pre_column = column

            ans[-1].append(val)

        return ans 
