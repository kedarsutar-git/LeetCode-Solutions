class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        validstr = 0
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(i)

            else:
                stack.pop()

                if(not stack):
                    stack.append(i)

                else:
                    validstr = max(validstr,i-stack[-1])

        return validstr