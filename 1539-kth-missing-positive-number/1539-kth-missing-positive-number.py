class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums)-1   
        while start<=end:
            mid = start + (end-start)//2
            miss = nums[mid] - (mid+1)
            if miss<k:
                start = mid+1
            else:
                end = mid-1
        return k + end + 1     