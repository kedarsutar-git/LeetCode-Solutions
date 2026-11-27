class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        # nums_set = set(nums)

        # count = 0
        # curr = 1
        # ans = 0

        # while(count<k):
        #     if curr not in nums_set:
        #         ans += curr
        #         count += 1

        #     curr += 1

        nums.sort()
        total = 0
        prev = 0
        for num in nums:
            if num ==prev:
                continue

            missing = num - prev - 1

            if missing>0:
                take = min(k,missing)
                total += (prev+1+prev+take) * take//2
                k -= take

                if k==0:
                    return total

            prev = num

        total += (prev + 1 + prev + k) *k//2
        return total



        return ans 




