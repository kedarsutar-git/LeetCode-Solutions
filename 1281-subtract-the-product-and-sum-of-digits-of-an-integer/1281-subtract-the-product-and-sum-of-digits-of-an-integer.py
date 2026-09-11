class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum = sum(int(digit) for digit in str(n))
        product = 1
        for num in str(n):
            digit = int(num)
            product = product*digit

        return product - Sum
            
        
        