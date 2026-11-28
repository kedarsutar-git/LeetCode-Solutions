class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        minnum = min(nums)
        maxnum = max(nums)
        ans = []
        for i in range(minnum,maxnum):
            if i in nums:
                continue

            if i not in nums:
                ans.append(i)

        return ans

            