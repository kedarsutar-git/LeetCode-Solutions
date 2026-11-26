class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base, mod = 100_003, 1_000_000_007
        power = [1] * (n + 1)
        prefix = [0] * (n + 1)

        for i, value in enumerate(nums):
            power[i + 1] = power[i] * base % mod
            prefix[i + 1] = (prefix[i] * base + value) % mod

        def has_unique_subarray(length: int) -> bool:
            frequency = {}
            for left in range(n - length + 1):
                right = left + length
                subarray_hash = (prefix[right] - prefix[left] * power[length]) % mod
                frequency[subarray_hash] = frequency.get(subarray_hash, 0) + 1
            return 1 in frequency.values()

        low, high = 1, n
        while low < high:
            middle = (low + high) // 2
            if has_unique_subarray(middle):
                high = middle
            else:
                low = middle + 1
        return low