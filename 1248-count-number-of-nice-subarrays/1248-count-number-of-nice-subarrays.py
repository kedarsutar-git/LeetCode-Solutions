class Solution:
    def Atmost(self,nums:List[int],k:int) ->int:
        right ,left = 0 ,0
        Sum = 0
        count = 0

        while(right<len(nums)):
            Sum += (nums[right]%2)

            while(Sum>k):
                Sum -= (nums[left]%2)
                left += 1

            count += (right - left + 1)
            right += 1

        return count         

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.Atmost(nums,k) - self.Atmost(nums,k-1)

        