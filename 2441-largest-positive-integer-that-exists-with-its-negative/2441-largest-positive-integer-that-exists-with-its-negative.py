class Solution:
    def findMaxK(self, nums: List[int]) -> int:
      
        count_map = {}
        for num in nums:
            count_map[num] = 1

        ans = -1
        for key in count_map:
            if(key>0 and -key in count_map):
                ans = max(ans,key)

        return ans 

            

