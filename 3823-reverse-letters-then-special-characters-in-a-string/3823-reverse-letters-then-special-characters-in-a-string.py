class Solution:
    def reverseByType(self, s: str) -> str:
        t = "abcdefghijklmnopqrstuvwxyz"
        x = "!@#$%^&*()"

        # reverse Letters
        start = 0
        end = len(s)-1
        s = list(s)
        while(start<end):
            if(s[start] in t and s[end] in t):
                s[start],s[end] = s[end],s[start]

                start+=1
                end  -=1

            elif(s[start] not in t):
                start+=1

            else:
                end-=1
        
        # reverse special characters
        start = 0
        end = len(s)-1
        while(start<end):
            if(s[start] in x and s[end] in x):
                 s[start],s[end] = s[end],s[start]

                 start +=1
                 end-=1

            elif(s[start] not in x):
                start+=1

            else:
                end-=1

        return "".join(s)




        