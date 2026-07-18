class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right = 0 , 0
        minlen = float("inf")
        Sum = 0
        while(right<len(nums)):
            Sum += nums[right]

            while(Sum>=target):

                minlen = min(minlen,right-left+1)
                Sum -= nums[left]
                left += 1
            right += 1

        if(minlen==float("inf")):
            return 0

        return minlen    








       

        

        

        



        