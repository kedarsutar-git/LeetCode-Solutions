class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        right ,left = 0,0
        maxlen = 0

        count_map = {}
        while(right<len(nums)):

            if nums[right] in count_map:
                count_map[nums[right]] += 1
            
            else:
                count_map[nums[right]] = 1
            
            while(count_map[nums[right]]>k):
                count_map[nums[left]] -=1
                left += 1

                
            if(count_map[nums[right]]<=k):

                length = right - left + 1

                maxlen = max(maxlen,length)

            right += 1
        return maxlen 

        