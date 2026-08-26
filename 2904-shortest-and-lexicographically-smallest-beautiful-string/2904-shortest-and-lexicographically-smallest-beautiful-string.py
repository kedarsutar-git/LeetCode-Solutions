class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        right,left = 0 ,0 
        res = ""
        count = 0
        while(right<len(s)):
            if(s[right]=="1"):
                count += 1

            while(count>k):
                if(s[left]=="1"):
                    count -= 1
                
                left += 1

            if(count==k):
                while(s[left]=="0"):
                    left += 1

                curr = s[left:right+1]

                if(res=="" or len(curr)<len(res) or len(curr)==len(res) and curr<res):
                    res = curr

            right += 1
        return res 
            
        
        