class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalsum = sum(nums)
        rightsum = 0
        leftsum = 0
        ans = []
        for i in range(len(nums)):
            rightsum = totalsum - leftsum - nums[i]

            ans.append(abs(leftsum-rightsum))

            leftsum += nums[i]

        return ans












# Find the total sum of the array.
# Maintain a running leftSum.
# For each index:
# rightSum = totalSum - leftSum - nums[i]
# answer[i] = abs(leftSum - rightSum)
# Update leftSum += nums[i]