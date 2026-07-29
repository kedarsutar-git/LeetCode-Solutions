class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:

        base = 0

        # Customers already satisfied
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]

        # Gain in first window
        gain = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                gain += customers[i]

        best = gain

        # Slide the window
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                gain += customers[i]

            if grumpy[i - minutes] == 1:
                gain -= customers[i - minutes]

            best = max(best, gain)

        return base + best
        