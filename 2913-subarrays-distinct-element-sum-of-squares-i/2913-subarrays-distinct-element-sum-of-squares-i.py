class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0
        s= set()
        all_subarray = []
        for i in range(len(nums)):
            current_subarray = []
            for j in range(i,len(nums)):
                current_subarray.append(nums[j])

                all_subarray.append(list(current_subarray))

        for num in all_subarray:
            s = set(num)
            count += len(s)**2 

        return count

'''
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
'''
