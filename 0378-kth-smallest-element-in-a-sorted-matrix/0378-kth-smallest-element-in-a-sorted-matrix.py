class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l.append(matrix[i][j])

        l.sort()
        count = 0
        for i in range(len(l)):
            count += 1
            if(count==k):
                ans = l[i]
        return ans




        