class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        right,left = 0,0
        currentavg =  0
        maxavg = float("-inf")

        while(right<len(nums)):
            currentavg += nums[right]
            

            if(right-left+1<k):
                right += 1

            elif(right-left+1==k):
                maxavg = max(maxavg,currentavg/k)

                currentavg -= nums[left]

                left += 1
                right += 1

        return maxavg   
'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        Max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum = window_sum -nums[i-k]+nums[i]

            Max_sum = max(Max_sum,window_sum)

        return Max_sum/k 
    
        '''