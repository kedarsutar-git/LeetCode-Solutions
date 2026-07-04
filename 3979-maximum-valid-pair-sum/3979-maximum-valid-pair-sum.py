class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        ans = float("-inf")
        Max = nums[0]
        for j in range(k,len(nums)):
            Max = max(Max,nums[j-k])

            ans = max(ans,Max+nums[j])

        return ans 
        
        