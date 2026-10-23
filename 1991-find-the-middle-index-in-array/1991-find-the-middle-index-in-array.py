class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        leftsum = 0
        totalsum = sum(nums)

        for index,num in enumerate(nums):
            totalsum -= num
            if(leftsum==totalsum):
                return index

            leftsum += num

        return -1
