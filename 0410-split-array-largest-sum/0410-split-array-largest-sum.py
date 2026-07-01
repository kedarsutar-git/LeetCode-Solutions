class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if(k>len(nums)):
            return -1


        start = max(nums)
        end = sum(nums)

        while(start<=end):
            mid = start +(end-start)//2

            Sum = 0
            split = 1

            for num in nums:
                if(Sum+num<=mid):
                    Sum +=num

                else:
                    split +=1

                    Sum = num

            if(split>k):
                start = mid+1

            else:
                end = mid-1

        return start                            
        