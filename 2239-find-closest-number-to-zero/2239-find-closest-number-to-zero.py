class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums:
            if(abs(num)<abs(ans)):
                ans = num

            elif(abs(num)==abs(ans)):
                ans = max(ans,num) 

        return ans            

            
        