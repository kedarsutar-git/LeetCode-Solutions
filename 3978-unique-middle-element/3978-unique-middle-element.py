class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        start = 0
        end = len(nums)-1

        mid = start + (end - start)//2

        count = 0
        for i in range(len(nums)):
            if(nums[mid]==nums[i]):
                count +=1

        if(count==1):
            return True 

        return False 
        
                
            
        