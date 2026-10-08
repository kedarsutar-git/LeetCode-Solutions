class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        i, j = 0, 0
        count = 0
        ans = ""

        while(i<len(s)):
            if(j<len(spaces) and count==spaces[j]):
                ans += " "
                j += 1

            else:
                ans += s[i]
                i += 1
                count += 1

        return ans


        