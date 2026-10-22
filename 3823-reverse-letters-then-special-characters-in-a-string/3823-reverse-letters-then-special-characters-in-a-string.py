class Solution:
    def reverseByType(self, s: str) -> str:
        t = "abcdefghijklmnopqrstuvwxyz"
        char = "!@#$%^&*()"

        start = 0
        end = len(s) - 1
        strarr = list(s)

        while(start<end):
            if(strarr[start] in t and strarr[end] in t):
                strarr[start],strarr[end] = strarr[end],strarr[start]

                start += 1
                end -= 1

            elif(strarr[start] not in t):
                start += 1

            else:
                end -= 1


        start = 0
        end = len(s) - 1

        while(start<end):
            if(strarr[start] in char and strarr[end] in char):
                strarr[start],strarr[end] = strarr[end],strarr[start]

                start += 1
                end -= 1

            elif(strarr[start] not in char):
                start += 1

            else:
                end -= 1

        return "".join(strarr)
