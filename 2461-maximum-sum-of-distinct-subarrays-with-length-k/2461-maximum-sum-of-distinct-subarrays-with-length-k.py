class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxsum = 0
        currentsum = 0
        right,left = 0,0
        Map ={}
        while(right<len(nums)):
                currentsum += nums[right]

                if nums[right] in Map:
                    Map[nums[right]] += 1

                else:
                    Map[nums[right]] = 1

                if(right-left+1==k):

                    if(len(Map)==k):

                        maxsum = max(maxsum,currentsum)
                    currentsum -= nums[left]
                    Map[nums[left]] -=1
                    
                    if Map[nums[left]] == 0:
                        del Map[nums[left]]

                    left += 1
                right += 1
        return maxsum



   

        