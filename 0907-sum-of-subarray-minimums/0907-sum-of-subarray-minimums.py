class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        # Next Smaller Element
        nse = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        # Previous Smaller or Equal Element
        psee = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                psee[i] = stack[-1]

            stack.append(i)

        # Calculate answer
        MOD = 10**9 + 7
        total = 0

        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i

            contribution = arr[i] * left * right

            total = (total + contribution) % MOD

        return total
        

        