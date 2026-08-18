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
        