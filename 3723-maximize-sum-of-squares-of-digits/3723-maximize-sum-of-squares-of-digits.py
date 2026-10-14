class Solution:
    def maxSumOfSquares(self, num: int, targetsum: int) -> str:
        if(targetsum > 9 * num):
            return ""

        nines = targetsum // 9
        remainder = targetsum % 9

        result = "9" * nines

        if(remainder):
            result += str(remainder)

        result += "0" * (num - len(result))

        return result

        