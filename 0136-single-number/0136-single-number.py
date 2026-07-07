'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans = ans ^ num

        return ans   

        '''  
           
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Map = {}
        for num in nums:
            if num in Map:
                Map[num]+=1

            else:
                Map[num]=1

        ans = 0
        for key,value in Map.items():
            if(value==1):
                ans = key

        return ans 


