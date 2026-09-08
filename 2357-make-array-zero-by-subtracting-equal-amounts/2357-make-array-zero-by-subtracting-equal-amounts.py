class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = []

        for value in nums:
            if value > 0:
                heapq.heappush(heap, value)

        operation = 0
        previous = 0

        while heap:
            value = heapq.heappop(heap)

            if value != previous:
                operation += 1
                previous = value

        return operation



'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opertion = 0
        while(sum(nums)!=0):
            for value in nums:
                if(value>0):
                    minnum = value 
                    break

            for i in range(len(nums)):
                if(nums[i]>0):
                    minnum = min(minnum,nums[i])
                
            for i in range(len(nums)):
                if(nums[i]>0):
                    nums[i] = nums[i] - minnum
                

            opertion += 1

        return opertion
'''