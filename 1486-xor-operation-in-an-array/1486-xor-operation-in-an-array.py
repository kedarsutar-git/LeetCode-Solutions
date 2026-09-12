class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = []
        for i in range(n):
            ans.append(start + 2*i)
        result = 0
        for num in ans:
            result ^= num

        return result 
        
        