class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]

        if(nums[0]!=nums[1]):
            return nums[0]

        if(nums[len(nums)-1]!=nums[len(nums)-2]):
            return nums[len(nums)-1] 

        start = 1
        end = len(nums) -2

        while(start<=end):
            mid = start +(end-start)//2

            if(nums[mid-1]!=nums[mid] and nums[mid+1]!=nums[mid]):
                return nums[mid]

            if(mid%2==1 and nums[mid-1]==nums[mid] or mid%2==0 and nums[mid+1]==nums[mid]):
                start = mid+1

            else:
                end = mid -1

        return -1                           