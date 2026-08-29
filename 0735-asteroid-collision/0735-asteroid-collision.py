class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            if(nums[i]>0):
                stack.append(nums[i])

            else:
                while(len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(nums[i])):
                    stack.pop()

                if(len(stack)==0 or stack[-1]<0):
                    stack.append(nums[i])

                elif(stack[-1]==abs(nums[i])):
                    stack.pop()

        return stack 
                
        