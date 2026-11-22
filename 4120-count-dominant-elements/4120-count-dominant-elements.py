class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        count = 0 
        for i in range(len(nums)):
            if i==0:
                if nums[i]>=nums[i+1]:
                    count += 1

            elif i==len(nums)-1:
                if nums[i]>=nums[i-1]:
                    count += 1

            else:
                if nums[i]*2>=(nums[i+1]+nums[i-1]):
                    count += 1

        return count 