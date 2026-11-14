class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minsum = float("inf")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if l<=len(nums[i:j])<=r:
                    currsum = sum(nums[i:j])
                    if currsum > 0:
                        minsum = min(minsum, currsum)

        if minsum != float("inf"):
            return minsum

        return -1 