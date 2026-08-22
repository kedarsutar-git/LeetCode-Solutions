class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(digits) for digits in str(n)]
        sumdights = sum(digits)
        productdigits = 1

        for num in digits:
            productdigits *= num

        if(n%(productdigits+sumdights)==0):
            return True 

        else:
            return False
