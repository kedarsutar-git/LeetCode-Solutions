class Solution:
    def findClosestElements(self, nums: list[int], k: int, target: int) -> list[int]:
        start, end = 0, len(nums) - k
        
        while(start < end):
            mid = start + (end - start) // 2
            
            if(target - nums[mid] > nums[mid + k] - target):
                start = mid + 1
            else:
                end = mid
                
        return nums[start : start + k]