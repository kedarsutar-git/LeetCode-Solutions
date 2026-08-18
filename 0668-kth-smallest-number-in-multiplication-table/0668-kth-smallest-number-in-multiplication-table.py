class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start = 0
        end = m*n

        while(start<end):
            mid = start + (end - start)//2

            count = 0
            for i in range(1,n+1):
                count += min(m,mid//i)

            if(count<k):
                start = mid+1
            else:
                end = mid
        
        return start
        

'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        matrix = []
        for i in range(1,n+1):
            row = []
            for j in range(1,m+1):
                row.append(i*j)

            matrix.append(row)

        arr =[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])
        
        arr.sort()

        count = 0
        ans  = 0
        for x in range(len(arr)):
            count += 1
            if(count==k):
                ans  = arr[x]

        return ans 
'''