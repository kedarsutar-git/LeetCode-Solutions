class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxlen = 0
        left,right =0,0
        zeros = 0

        while(right<len(nums)):
            if(nums[right]==0):
                zeros +=1

            while(zeros>1):
                if(nums[left]==0):
                    zeros -=1

                left += 1

            length = right-left 

            maxlen = max(maxlen,length)

            right += 1
        return maxlen