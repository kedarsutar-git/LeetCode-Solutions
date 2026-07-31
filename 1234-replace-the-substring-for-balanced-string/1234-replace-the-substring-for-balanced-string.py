from collections import defaultdict

class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s) // 4
        count_map = defaultdict(int)

        for char in s:
            count_map[char] += 1

        if (count_map["Q"] == target and count_map["W"] == target and count_map["E"] == target and count_map["R"] == target):
            return 0

        left,right = 0,0
        minlen = len(s)

        while(right<len(s)):
            count_map[s[right]] -= 1

            while (left <= right and count_map["Q"] <= target and count_map["W"] <= target and count_map["E"] <= target and count_map["R"] <= target):

                minlen = min(minlen, right - left + 1)
                count_map[s[left]] += 1
                left += 1
            right +=1


        return minlen