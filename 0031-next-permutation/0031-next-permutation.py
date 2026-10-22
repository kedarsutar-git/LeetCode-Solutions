class Solution:
    def nextPermutation(self, nums: List[int]) -> list[int]:
        pivit = -1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i+1]>nums[i]):
                pivit = i
                break

        if(pivit==-1):
            i = 0
            j = len(nums)-1

            while(i<=j):
                nums[i],nums[j] = nums[j],nums[i]

                i += 1
                j -= 1

            return nums


        # find the number that exact gerter then pivit 

        for i in range(len(nums)-1,-1,-1):
            if(nums[i]>nums[pivit]):
                nums[i],nums[pivit] = nums[pivit],nums[i]
                break

        i = pivit + 1
        j = len(nums) - 1

        while(i<=j):
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1

        return nums
