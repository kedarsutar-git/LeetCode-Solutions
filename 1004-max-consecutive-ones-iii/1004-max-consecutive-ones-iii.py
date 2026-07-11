class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0 
        left , right = 0 , 0
        zeros = 0

        while(right<len(nums)):
            if(nums[right]==0):
                zeros +=1

            while(zeros>k):
                if(nums[left]==0):
                    zeros -= 1

                left += 1

            if(zeros<=k):
                length = right - left + 1
                max_len = max(max_len,length)

            right += 1

        return max_len                    


        