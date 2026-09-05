class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            maxnum = nums[0]
            minnum = nums[i]

            for j in range(0,i+1):
                maxnum = max(maxnum,nums[j])

            for j in range(i,len(nums)):
                minnum = min(minnum,nums[j])

            if(maxnum-minnum<=k):
                return i

        return -1 