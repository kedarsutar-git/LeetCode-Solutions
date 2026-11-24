class Solution:
    def maxLength(self, nums: List[int]) -> int:
        longest = 0
        for left in range(len(nums)):
            product = 1
            gcd = 0
            lcm = 1

            for right in range(left, len(nums)):
                value = nums[right]
                product *= value
                gcd = self.gcd(gcd, value)
                lcm = lcm * value // self.gcd(lcm, value)

                if product == gcd * lcm:
                    longest = max(longest, right - left + 1)

        return longest


    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)