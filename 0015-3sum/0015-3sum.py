class Solution:
    def threeSum(self,nums:list[int]) ->list[list[int]]:
        temp = []
        nums.sort()
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue 
            j = i+1
            k = len(nums)-1
            while(j<k):
                Sum = nums[i]+nums[j]+nums[k]
                if(Sum<0):
                    j+=1

                elif(Sum>0):
                    k-=1

                else:
                    temp.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1

        return temp                                
