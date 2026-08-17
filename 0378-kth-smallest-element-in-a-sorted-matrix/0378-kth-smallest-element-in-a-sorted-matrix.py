class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left  = matrix[0][0]
        right = matrix[-1][-1]

        while(left<right):
            mid = left + (right-left)//2

            s = 0
            c = len(matrix)-1
            for row in matrix:
                while(c>=0 and row[c]>mid):
                    c -=1
                s += c+1

            if(s<k):
                left = mid + 1
            
            else:
                right = mid
        
        return left 




        