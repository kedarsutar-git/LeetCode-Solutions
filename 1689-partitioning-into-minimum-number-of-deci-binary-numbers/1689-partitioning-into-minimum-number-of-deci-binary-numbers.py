class Solution:
    def minPartitions(self, n: str) -> int:
        minnum = float("-inf")
        
        for i in range(len(n)):
            minnum = max(minnum,int(n[i]))

        return minnum