class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        start = 0
        end = len(s)-1
        s = list(s)
        while(start<=end):
            if(s[start] in char and s[end] in char):
                s[start],s[end] = s[end],s[start]

                start+=1
                end-=1

            elif(s[start] not in char):
                start+=1

            elif(s[end] not in char):
                end -=1

        return "".join(s)

                    
