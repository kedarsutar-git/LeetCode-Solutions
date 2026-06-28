class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        temp = []
        for i in range(1,len(mountain)-1):
            if(mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]):
                temp.append(i)

        return temp        

        