class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            product = 1
            for j in range(i,len(nums)):
                product = product * nums[j]

                if(product<k):
                    count +=1

                else:
                    break 

        return count                 
        