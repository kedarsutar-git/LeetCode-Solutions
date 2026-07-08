'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq = 0
        ans = 0
        for i in range(len(nums)):
            if(frq==0):
                ans = nums[i]

            if(ans==nums[i]):
                frq+=1
            else:
                frq-=1
        return ans                
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_map = {}
        for num in nums:
            if( num in count_map ):
                count_map[num] += 1

            else:
                count_map[num] = 1

        ans  = 0 
        for key,value in count_map.items():
            if(value>n/2):
                ans = key 

        return ans 


        