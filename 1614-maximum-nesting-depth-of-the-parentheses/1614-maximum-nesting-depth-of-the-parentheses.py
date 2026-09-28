class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0
        for brac in s:
            if(brac=="("):
                current_depth += 1
                max_depth = max(current_depth,max_depth)

            elif(brac==")"):
                current_depth -= 1

        return max_depth

