import math

class Solution:
    def minEatingSpeed(self, piles, h):
        start ,end = 1 , max(piles)

        while(start<=end):
            mid = start + (end - start)//2

            TotalH = 0

            for bananas in piles:
                TotalH += math.ceil(bananas/mid)

            if(TotalH<=h):
                end = mid - 1

            else:
                start = mid + 1

        return start


