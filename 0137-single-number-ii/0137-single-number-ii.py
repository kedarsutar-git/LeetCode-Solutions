class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num]+=1

            else:
                count_map[num]=1

        ans = 0
        for key,value in count_map.items():
            if(value==1):
                ans = key

        return ans 



            
        