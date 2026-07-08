class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = {}

        for letter in s:
            if letter in count_map:
                count_map[letter] += 1

            else:
                count_map[letter] = 1


        
        for i in range(len(s)):
            if(count_map[s[i]]==1):
                return i

        return -1               





        