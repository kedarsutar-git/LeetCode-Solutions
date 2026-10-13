class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        array = [x*x for x in nums]
        arr = sorted(array)

        n = len(arr)
        pos = (n+1)//2

        return sum(arr[n-pos:]) - sum(arr[:n-pos])
        
    
        