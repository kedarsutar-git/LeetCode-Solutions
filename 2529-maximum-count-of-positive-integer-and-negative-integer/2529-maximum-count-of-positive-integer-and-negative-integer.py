class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        poscount = 0
        negcount = 0

        for i in range(len(nums)):
            if(nums[i]<0):
                negcount +=1

            elif(nums[i]>0):
                poscount +=1

        return max(poscount,negcount)        
                    

        