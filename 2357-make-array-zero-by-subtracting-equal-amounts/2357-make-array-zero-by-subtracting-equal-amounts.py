class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opertion = 0
        while(sum(nums)!=0):
            for value in nums:
                if(value>0):
                    minnum = value 
                    break

            for i in range(len(nums)):
                if(nums[i]>0):
                    minnum = min(minnum,nums[i])
                
            for i in range(len(nums)):
                if(nums[i]>0):
                    nums[i] = nums[i] - minnum
                

            opertion += 1

        return opertion