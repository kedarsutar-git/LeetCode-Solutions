class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        Max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum = window_sum -nums[i-k]+nums[i]

            Max_sum = max(Max_sum,window_sum)

        return Max_sum/k    

        