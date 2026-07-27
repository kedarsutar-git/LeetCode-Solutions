class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        right,left = 0,0
        count_map ={}
        maxnum =max(nums)

        while(right<len(nums)):
            if(nums[right] in count_map):
                count_map[nums[right]] +=1
            
            else:
                count_map[nums[right]] =1

            while(count_map.get(maxnum,0)>=k):
                count += (len(nums)-right)

                count_map[nums[left]] -=1

                if(count_map[nums[left]]==0):
                    del count_map[nums[left]]

                left +=1
            right +=1
        return count

'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        maxnum = max(nums)
        for i in range(len(nums)):
            count_map = {}
            for j in range(i,len(nums)):
                if nums[j] in count_map:
                    count_map[nums[j]] +=1
                
                else:
                    count_map[nums[j]] = 1
                
                if(count_map.get(maxnum,0)>=k):
                    count +=1
        
        return count
    


        
        '''