class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0 
        Open = 0
        for i in range(len(s)):
            if(s[i]=="("):
                Open += 1

            else:
                if(Open>0):
                    Open -= 1

                else:
                    ans += 1

        return ans + Open

    