class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while(left<right):
                curr_sum = nums[i] + nums[left] + nums[right]

                if(abs(target-curr_sum)<abs(target-ans)):
                    ans = curr_sum
                
                if(curr_sum<target):
                    left += 1
                
                elif(curr_sum>target):
                    right -=1
                
                else:
                    return target
        return ans 


      