class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for digits in nums:

            while(stack and k>0 and stack[-1]>digits):
                stack.pop()
                k -= 1

            stack.append(digits)

        while(stack and k>0):
            stack.pop()
            k-=1

        if(not stack):
            return "0"

        res = ""

        while(stack):
            res += stack.pop()

        res = res.rstrip('0')

        res = res[::-1]

        if(not res):
            return "0"

        return res
        
        