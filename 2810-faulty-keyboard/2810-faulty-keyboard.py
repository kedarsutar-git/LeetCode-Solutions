class Solution:
    def finalString(self, s: str) -> str:
        S  = []

        for i in range(len(s)):
            if(s[i]!="i"):
                S.append(s[i])

            if(s[i]=="i"):
                S.reverse()

               

        return "".join(S)




            
        