class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special case
        if dividend == divisor:
            return 1

        # Determine the sign of the answer
        sign = True
        if (dividend >= 0 and divisor < 0) or \
           (dividend < 0 and divisor > 0):
            sign = False

        # Work with positive numbers
        n = abs(dividend)
        d = abs(divisor)

        ans = 0

        # Repeatedly subtract using bit manipulation
        while n >= d:
            count = 0

            while n >= (d << (count + 1)):
                count += 1

            ans += (1 << count)
            n -= (d << count)

        # Apply the sign
        if not sign:
            ans = -ans

        # Handle overflow
        if ans > INT_MAX:
            return INT_MAX

        if ans < INT_MIN:
            return INT_MIN

        return ans