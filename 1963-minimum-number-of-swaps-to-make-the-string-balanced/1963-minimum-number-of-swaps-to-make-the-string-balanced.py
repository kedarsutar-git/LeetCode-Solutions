class Solution:
    def minSwaps(self, s: str) -> int:
        max_imbalance = 0
        balance = 0
        for i in range(len(s)):
            if(s[i]=="["):
                balance += 1

            else:
                balance -= 1

            max_imbalance = min(max_imbalance,balance)

        return (-max_imbalance+1)//2

        