class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = 0
        doubleSum = 0
        for num in nums:
            if(len(str(num))==1):
                singleSum += int(num)
            if(len(str(num))==2):
                doubleSum += int(num)

        return singleSum != doubleSum

        