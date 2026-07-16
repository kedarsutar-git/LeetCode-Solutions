class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        count_map = {}
        for char in t:
            if char in count_map:
                count_map[char] +=1

            else:
                count_map[char] = 1

        left,right = 0, 0
        count = 0
        startindex = -1
        minlen = float("inf")

        while(right<n):
            if(count_map.get(s[right], 0)>0):
                count += 1

            count_map[s[right]] = count_map.get(s[right],0) - 1

            while(count==m):
                if(right-left+1<minlen):
                    minlen = right-left+1
                    startindex = left

                count_map[s[left]]  = count_map.get(s[left],0) + 1

                if(count_map[s[left]]>0):
                    count -=1

                left +=1
            right +=1

        if startindex == -1:
            return ""

        return s[startindex:startindex + minlen]

                             


        