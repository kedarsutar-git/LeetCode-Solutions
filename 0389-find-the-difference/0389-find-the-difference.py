class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in t:
            if( t.count(x) > s.count(x)):
                return (x)
               


        