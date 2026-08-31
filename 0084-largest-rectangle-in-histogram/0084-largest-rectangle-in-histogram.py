class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        def findNSE():
            n = len(nums)
            nse = [n] * n
            stack = []

            for i in range(n - 1, -1, -1):

                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if stack:
                    nse[i] = stack[-1]

                stack.append(i)

            return nse

        def findPSEE():
            n = len(nums)
            psee = [-1] * n
            stack = []

            for i in range(n):

                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()

                if stack:
                    psee[i] = stack[-1]

                stack.append(i)

            return psee

        NSE = findNSE()
        PSEE = findPSEE()

        maxnum = 0

        for i in range(len(nums)):
            area = nums[i] * (NSE[i] - PSEE[i] - 1)
            maxnum = max(maxnum, area)

        return maxnum




        