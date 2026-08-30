class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        totalsum = 0
        for i in range(len(nums)):
            minnum , maxnum = nums[i],nums[i]
            for j in range(i,len(nums)):
                minnum = min(minnum,nums[j])
                maxnum = max(maxnum,nums[j])

                totalsum += (maxnum-minnum)

        return totalsum                
        