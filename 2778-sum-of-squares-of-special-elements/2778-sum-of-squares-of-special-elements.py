class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = 0
        for i in range(1,len(nums)+1):
            if(n%i==0):
                Sum +=nums[i-1]**2

        return Sum        

                  


        