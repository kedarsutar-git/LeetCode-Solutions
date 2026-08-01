from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        curr_sum = 0
        left,right = 0,0

        window = 2*k+1
        ans = [-1]*len(nums)

        

        if(window>len(nums)):
            return ans 

        while(right<len(nums)):
            curr_sum += nums[right]

            while(right-left+1>window):
                curr_sum -= nums[left]
                left += 1

            if(right - left +1==window):
                center = (right+left)//2

                ans[center] = curr_sum//window 

            right += 1
        return ans 



        