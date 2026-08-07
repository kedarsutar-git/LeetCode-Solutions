class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxnum = max(max(nums),0)
        setnum = set(nums)

        for i in range(1,maxnum+2):
            if i not in setnum:
                return i



        