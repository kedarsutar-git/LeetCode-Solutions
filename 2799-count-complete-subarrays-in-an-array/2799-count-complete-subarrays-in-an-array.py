class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        totalDistinct = len(set(nums))

        left = 0
        right = 0
        count = 0
        freq = {}

        while right < len(nums):

            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1

            while len(freq) == totalDistinct:

                # Every subarray starting at 'left' and ending at
                # right, right+1, ..., n-1 will remain complete.
                count += len(nums) - right

                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            right += 1

        return count





'''
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count_map1 = {}
        for num in nums:
            if( num in count_map1):
                count_map1[num] += 1

            else:
                count_map1[num]  = 1

        count = 0

        for i in range(len(nums)):
            count_map2 = {}
            for j in range(i,len(nums)):
                
                if(nums[j] in count_map2):
                    count_map2[nums[j]] += 1

                else:
                    count_map2[nums[j]] = 1

                if(len(count_map1)==len(count_map2)):
                    count += 1

        return count                     
                                       
         '''              