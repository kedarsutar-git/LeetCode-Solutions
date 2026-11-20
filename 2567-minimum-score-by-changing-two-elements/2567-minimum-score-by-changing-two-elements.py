class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)
        if n==3:
            return 0
        else:
            nums.sort()
            for i in range(3):
                score = nums[n-3+i] - nums[i]
                res = min( res, score )
        return res      


