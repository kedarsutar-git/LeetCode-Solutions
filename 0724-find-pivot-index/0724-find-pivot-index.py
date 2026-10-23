class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftsum = 0
        totalsum = sum(nums)
        for index,num in enumerate(nums):
            totalsum -= num
            if(totalsum==leftsum):
                return index

            leftsum += num

        return -1
