class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        pairscount = 0
        count_map = {}
        right,left = 0,0 
        while(right<len(nums)):

            if(nums[right] in count_map):
                pairscount += count_map[nums[right]]
                count_map[nums[right]] += 1
            
            else:
                count_map[nums[right]] = 1

            while(pairscount>=k):
                count_map[nums[left]] -=1
                pairscount -= count_map[nums[left]]
                left += 1

            
            count += left
            
            right += 1
            
        return count
        