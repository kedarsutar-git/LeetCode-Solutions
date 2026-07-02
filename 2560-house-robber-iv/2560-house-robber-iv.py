class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        start = min(nums)
        end = max(nums)
        ans = -1
        while(start<=end):
            mid = start + (end - start)//2

            if(self.is_valid(nums,mid,k)):
                ans = mid
                end = mid - 1

            else:
                start = mid + 1

        return ans 

    def is_valid(self,nums, mid,k):
        count = 0
        i = 0

        while(i < len(nums)):
            if nums[i] <= mid:
                count += 1
                i += 2
            else:
                i += 1

        return count >= k            


        