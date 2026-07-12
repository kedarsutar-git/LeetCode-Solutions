class Solution:
    def Atmost(self, nums: List[int], goal: int) -> int:
        if(goal<0):
            return 0

        left ,right = 0, 0
        Sum ,count = 0, 0

        while(right<len(nums)):
            Sum += nums[right]

            while(Sum>goal):
                Sum -= nums[left]
                left += 1

            
            count += (right - left + 1)

            right += 1

        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.Atmost(nums,goal) - self.Atmost(nums,goal-1)

        