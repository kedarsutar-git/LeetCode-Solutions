class Solution:
    def twoSum(self, nums: list[int], target:int) -> list[int]: 
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []            
        