class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        right,left = 0 ,0 
        maxsum = 0 
        currentsum = 0
        count_map = {}
        while(right<len(nums)):
            currentsum += nums[right]
            
            if(nums[right] in count_map):
                count_map[nums[right]] += 1

            else:
                count_map[nums[right]] = 1

            if(right-left+1==k):
                if(len(count_map)>=m):
                    maxsum = max(maxsum,currentsum)

                count_map[nums[left]] -=1

                currentsum -= nums[left]

                if(count_map[nums[left]]==0):
                    del count_map[nums[left]]

                left += 1
            
            right += 1
            
        return maxsum





        