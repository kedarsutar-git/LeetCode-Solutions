class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pre = 0
        for token in s.split():
            if token.isdigit():
                curr = int(token)

                if curr <= pre:
                    return False
                else:
                    pre = curr
        return True




