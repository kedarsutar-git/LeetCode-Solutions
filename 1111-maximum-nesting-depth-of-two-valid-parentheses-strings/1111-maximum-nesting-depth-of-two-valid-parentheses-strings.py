class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0]*len(seq)
        depth = 0
        for i in range(len(seq)):
            if(seq[i]=="("):
                depth += 1
                ans[i] = depth%2
            else:
                ans[i] = depth%2
                depth -= 1

        return ans         