class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = []
        
        for num in nums:
            digits_sum = sum(int(d) for d in str(num))

            arr.append(digits_sum)

        temp = [(arr[i], nums[i], i) for i in range(len(nums))]

        temp.sort()  # sorts by digit sum, then value

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or temp[i][2] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = temp[j][2]
                cycle += 1

            swaps += cycle - 1

        return swaps

    


            
        