class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count_map = {}
        while(right<len(nums)):
            if(right-left+1==k):
                temp = set()

                i = left
                while(i<=right):
                    temp.add(nums[i])
                    i+=1
                
                for num in temp:
                    if num in count_map:
                        count_map[num] += 1

                    else:
                        count_map[num] = 1

                left += 1
            right += 1

        ans  = -1
        for num,frq in count_map.items():
            if(frq==1):
                ans = max(ans,num)

        return ans
        
            


        
        

        