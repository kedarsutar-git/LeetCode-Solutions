class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
      
        Maxones,results = 0, 0
        for num in nums:
            if(num==1):
                results += 1
                Maxones = max(Maxones,results)

            else:
                results = 0

        return Maxones
            