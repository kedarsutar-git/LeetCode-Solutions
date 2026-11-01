class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minnum = min(nums)
        Sum = 0

        for i in range(len(nums)):
            Sum = Sum + nums[i] - minnum

        return Sum
