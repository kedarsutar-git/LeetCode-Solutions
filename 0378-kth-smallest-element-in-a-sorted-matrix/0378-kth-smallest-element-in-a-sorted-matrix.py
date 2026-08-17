class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left  = matrix[0][0]  # smallest number in the matrix 
        right = matrix[len(matrix)-1][len(matrix)-1] # largest number in the matrix 

        while(left<right):
            mid = left + (right-left)//2

            count = 0
            row = len(matrix)-1
            col = 0
            while(row>=0 and col<len(matrix)):
                if(matrix[row][col]<=mid):
                    count += row + 1
                    col += 1
                
                else:
                    row -= 1

            if(count<k):
                left = mid + 1
            
            else:
                right = mid
        
        return left 




        