class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        Sum1,Sum2 = 0,0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i==j):
                    Sum1 += mat[i][j]
                
                if(i+j==len(mat)-1 and i!=j):
                    Sum2 += mat[i][j]

        return Sum1+Sum2

        