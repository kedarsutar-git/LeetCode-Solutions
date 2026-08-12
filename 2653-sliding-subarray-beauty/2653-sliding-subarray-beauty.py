class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        arr = []
        right,left = 0,0
        count_frq = defaultdict(int)

        while(right<len(nums)):

            if(nums[right]<0):
                count_frq[-nums[right]] += 1

            if(right-left+1>k):
                if(nums[left]<0):
                    count_frq[-nums[left]] -=1

                left += 1

            if(right-left+1==k):
                count = 0

                for i in range(50,0,-1):
                    count += count_frq[i]

                    if(count>=x):
                        arr.append(-i)

                        break

                if(count<x):
                    arr.append(0)
            right += 1

            
        return arr

            

            


        