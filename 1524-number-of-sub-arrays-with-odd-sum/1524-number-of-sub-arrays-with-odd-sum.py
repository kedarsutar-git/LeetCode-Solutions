class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = 0
        even = 0
        ans = 0 
        MOD = 1e9 + 7
        for num in arr:
            if num%2==0:
                even += 1

            else:
                odd,even = even+1,odd

            ans = (ans+odd)%MOD

        return int(ans)
        