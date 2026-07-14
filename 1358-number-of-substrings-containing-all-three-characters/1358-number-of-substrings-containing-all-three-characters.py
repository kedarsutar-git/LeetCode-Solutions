class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0 
        right, left = 0, 0
        a, b, c =0, 0, 0
        while(right<len(s)):
            if(s[right]=="a"):
                a += 1

            elif(s[right] =="b"):
                b += 1

            else:
                c += 1

            while(a>0 and b> 0 and c>0):
                count += (len(s)-right)
                if(s[left]=="a"):
                    a -= 1

                elif(s[left]=="b"):
                    b -= 1

                else:
                    c -= 1

                left += 1

            right += 1

        return count
                

               

        