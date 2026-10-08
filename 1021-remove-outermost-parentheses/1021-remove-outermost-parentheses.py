class Solution:
    def removeOuterParentheses(self, s):
        count = 0
        ans = ""
        for char in s:
            if(char =="("):
                if(count>0):
                    ans += char

                count += 1

            else:
                count -= 1

                if(count>0):
                    ans += char

        return ans      
 