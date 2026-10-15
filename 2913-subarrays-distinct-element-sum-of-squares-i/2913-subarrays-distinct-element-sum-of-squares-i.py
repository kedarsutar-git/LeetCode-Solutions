class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s = set()
        count = 0
        ans = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                subarray = []
                for k in range(i,j+1):
                    subarray.append(nums[k])

                ans.append(subarray)

        for num in ans:
            s = set(num)
            count += len(s)**2

        return count 
        