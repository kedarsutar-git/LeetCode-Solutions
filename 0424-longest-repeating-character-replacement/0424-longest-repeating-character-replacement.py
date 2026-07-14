class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Map = {}
        left, right = 0, 0
        max_freq, max_len = 0, 0

        while(right<len(s)):
            Map[s[right]] = Map.get(s[right],0) + 1

            max_freq = max(max_freq,Map[s[right]])

            while(right-left + 1) - max_freq>k:
                Map[s[left]] -= 1

                left += 1

            max_len = max(max_len,right-left+1)

            right += 1

        return max_len
                


        