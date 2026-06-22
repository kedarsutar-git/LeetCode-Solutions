class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s)-1
        t = "aeiouAEIOU"
        while(start<end):
            if(s[start] in t and s[end] in t):
                s[start],s[end] = s[end],s[start]

                start+=1
                end -=1

            elif(s[start] not in t):
                start+=1

            elif(s[end] not in t):
                end-=1
        return "".join(s)

            
            


        