class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end  = len(nums)-1

        ans = float('inf')
        while(start<=end):

            if(nums[start]<nums[end]):
                ans = min(ans,nums[start])
                break

            mid = start+(end-start)//2
            ans = min(ans,nums[mid])

            if(nums[start]<nums[mid]):
                ans = min(ans,nums[start])

                start = mid+1

            elif(nums[start]>nums[mid]):
                end = mid

            else:
                start +=1


        return ans             

        