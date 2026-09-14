class Solution:
    def fun(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True

    def firstPalindrome(self, words):
        for s in words:
            if self.fun(s):
                return s

        return ""
        