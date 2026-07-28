class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        right,left = 0,0
        currentsum = 0
        maxlen = -1
        target = sum(nums) - x
        if(target<0):
            return -1 

        if(target==0):
            return len(nums)

        while(right<len(nums)):
            currentsum +=nums[right]

            while(currentsum>target):
                currentsum -= nums[left]
                left+=1

            if(currentsum==target):
                maxlen = max(maxlen,right-left+1)

                
                
            right +=1
        if(maxlen!=-1):
            return len(nums) -maxlen
        return -1 
        


            
        
        