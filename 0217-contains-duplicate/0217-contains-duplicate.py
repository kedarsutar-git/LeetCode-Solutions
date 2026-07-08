'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True 

        return False        

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1

            else:
                count_map[num] = 1

        ans = 0

        for key , value in count_map.items():
            if(value>=2):
                return True 

        return False 
