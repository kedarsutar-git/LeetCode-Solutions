class Solution:
    def largestRectangleArea(self, heights):

        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                area = height * width

                max_area = max(max_area, area)

            stack.append(i)

        return max_area

    def maximalRectangle(self, matrix):

        if not matrix:
            return 0

        m = len(matrix[0])

        height = [0] * m

        max_area = 0

        for row in matrix:
            for i in range(m):

                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0

            max_area = max(max_area,self.largestRectangleArea(height))

        return max_area