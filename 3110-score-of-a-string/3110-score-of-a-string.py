class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = []
        for i in range(len(s)):
            ans.append(ord(s[i]))

            print(ans)
        first = 0
        second = 1
        diff = 0
        while(second<len(ans)):
            diff += abs(ans[first] - ans[second])

            first += 1
            second += 1

        return diff


            