class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        if(sum(candies)<k):
            return 0

        start = 1
        end = max(candies)
        ans = -1

        while(start<=end):
            mid = start + (end - start)//2

            if(self.isValid(candies,mid,k)):
                ans = mid
                start = mid + 1

            else:
                end = mid - 1

        return ans 


    def isValid(self,candies,mid,k):
        children = 0
        for x in candies:
            children += x//mid

        if(children>=k):
            return True 

        return False 
            
            



