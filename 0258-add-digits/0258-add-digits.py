class Solution:
    def addDigits(self, num: int) -> int:

        while(num>=10):
            total = 0
            for x in str(num):
                total += int(x)
            num = total
        return num
        