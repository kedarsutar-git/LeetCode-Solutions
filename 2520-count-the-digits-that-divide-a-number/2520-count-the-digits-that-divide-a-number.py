class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for digits_char in str(num):
            digit = int(digits_char)
            if(digit!=0 and num%digit==0):
                count += 1
        
        return count 


        