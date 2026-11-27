class Solution:
    def sumAndMultiply(self, n: int) -> int:
        strnum = str(n)
        nonzeronum = ""

        if n == 0:
            return 0 
            
        for i in range(len(strnum)):
            if strnum[i] != "0":
                nonzeronum += strnum[i]


        sumdits = sum(int(dight) for dight in nonzeronum)

        return sumdits * int(nonzeronum)
        


            
