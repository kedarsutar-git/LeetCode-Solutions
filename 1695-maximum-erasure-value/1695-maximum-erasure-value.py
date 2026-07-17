class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        right ,left = 0, 0
        maxscore = 0
        current_score = 0
        s = set()
        while(right<len(nums)):

            while(nums[right] in s):
                s.remove(nums[left])
                current_score -= nums[left]

                left += 1

            s.add(nums[right])
            current_score += nums[right]

            maxscore = max(maxscore,current_score)

            right +=1
        return maxscore


