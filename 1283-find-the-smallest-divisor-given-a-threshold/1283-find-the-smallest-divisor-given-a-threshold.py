import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start , end =  1 , max(nums) 
        ans  = 1

        while(start<=end):
            mid = start + (end - start)//2
            Sum = 0
            
            for num in nums:
                Sum += math.ceil(num/mid)

            if(Sum<=threshold):
                ans  = mid
                end = mid - 1

            else:
                start = mid + 1

        return ans               


        