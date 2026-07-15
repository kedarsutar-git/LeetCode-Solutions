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
                                       
                       