class Solution:
    def arrayRankTransform(self, nums: list[int]) -> list[int]:
        temp = sorted(set(nums))
        Rank = {}
        for i ,num in enumerate(temp):
            Rank[num] = i+1

        ans = []
        for num in nums:
            ans.append(Rank[num])

        return ans 
