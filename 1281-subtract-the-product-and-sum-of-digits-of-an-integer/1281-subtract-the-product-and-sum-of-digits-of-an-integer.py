class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum = 0
        product = 1
        for num in str(n):
            digit = int(num)
            product = product*digit
            Sum += digit

        return product - Sum
            
        
        