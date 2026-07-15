class Solution:
    def Atmost(self,nums:List[int],k:int) ->int:
        count = 0
        right, left = 0, 0
        count_map = {}
        while(right<len(nums)):
            if nums[right] in count_map:
                count_map[nums[right]] += 1

            else:
                count_map[nums[right]] = 1

            while(len(count_map)>k):

                count_map[nums[left]] -=1

                if(count_map[nums[left]]==0):
                    del count_map[nums[left]]

                left += 1

            count += (right -left +1)

            right += 1

        return count 
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        return self.Atmost(nums,k) - self.Atmost(nums,k-1)
                            
        