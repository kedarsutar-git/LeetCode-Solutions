class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        right,left = 0,0
        ans = float("inf")
        white = 0
        while(right<len(blocks)):

            if(blocks[right]=="W"):
                white += 1
            length = right -left + 1
            if(length==k):
                ans = min(ans,white)

                if(blocks[left]=="W"):
                    white -= 1
                    
                left += 1

            right += 1

        return ans     

'''
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float("inf")
        for i in range(len(blocks)):
            white = 0
            for j in range(i,len(blocks)):
                length = j - i + 1
                if(blocks[j]=="W"):
                    white +=1

                length = j- i+1
                if(length==k):
                    ans = min(ans,white)
                    break

        return ans   
         '''



                    




        

        