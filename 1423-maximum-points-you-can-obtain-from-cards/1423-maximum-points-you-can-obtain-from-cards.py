class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftsum, rightsum = 0, 0
        maxsum = 0

        for i in range(k):
            leftsum += cardPoints[i]

            maxsum = leftsum

        rightindex = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            leftsum -= cardPoints[i]

            rightsum += cardPoints[rightindex]    

            rightindex -= 1

            maxsum = max(maxsum,rightsum+leftsum)

        return maxsum    