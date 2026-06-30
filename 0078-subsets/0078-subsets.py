class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = 1<<n
        ans  = []
        for num in range(subset):
            temp = []

            for i in range(n):
                if(num & (1<<i)):
                    temp.append(nums[i])

            ans.append(temp)
            
        return ans 
        