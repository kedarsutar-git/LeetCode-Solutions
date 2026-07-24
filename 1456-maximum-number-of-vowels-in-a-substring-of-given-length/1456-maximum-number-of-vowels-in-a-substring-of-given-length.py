class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        right,left = 0,0
        currentcount,maxcount =0,0

        while(right<len(s)):

            if s[right] in vowels:
                currentcount += 1

            if(right-left+1==k):
                maxcount = max(maxcount,currentcount)

                if(s[left] in vowels):
                    currentcount -= 1

                left += 1

            right += 1 

        return maxcount       


        