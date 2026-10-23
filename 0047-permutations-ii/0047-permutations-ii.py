class Solution:
    def getper(self,nums:list[int],index:int,ans:list[int]):
        if(index==len(nums)):
            ans.append(nums[:])
            return 

        s = set()
        for i in range(index,len(nums)):
            if(nums[i] in s):
                continue

            s.add(nums[i])

            nums[index],nums[i] = nums[i],nums[index]
            self.getper(nums,index+1,ans)

            nums[index],nums[i] = nums[i],nums[index]

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.getper(nums,0,ans)
        return ans 