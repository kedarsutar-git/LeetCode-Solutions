class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minrow = []
        maxcol = []

        for i in range(len(matrix)):
            minnum = matrix[i][0]

            for j in range(len(matrix[0])):
                if(matrix[i][j]<minnum):
                    minnum = matrix[i][j]

            minrow.append(minnum)

        for j in range(len(matrix[0])):
            maxnum = matrix[0][j]

            for i in range(len(matrix)):
                if(matrix[i][j]>maxnum):
                    maxnum = matrix[i][j]

            maxcol.append(maxnum)

        ans = []
        for num in minrow:
            if num in maxcol:
                ans.append(num)

        return ans 


        

        