class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        temp = [-1]*len(nums)

        for i in range(len(nums)):
            for j in range(1,len(nums)):
                index = (i+j)%len(nums)

                if(nums[index]>nums[i]):
                    temp[i] = nums[index]
                    break
        return temp

        
        