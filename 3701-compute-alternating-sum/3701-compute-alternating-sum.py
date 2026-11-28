class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        evenindexnum = 0
        oddindexnum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                evenindexnum += nums[i]

            if i % 2 != 0:
                oddindexnum += nums[i]

        return evenindexnum - oddindexnum
