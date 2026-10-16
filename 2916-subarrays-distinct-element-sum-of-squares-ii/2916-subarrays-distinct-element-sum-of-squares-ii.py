class Solution:
    def sumCounts(self, nums):
        last = {}  # last occurrence of a value
        index = []  # indices of last occurrences, sorted
        totalsum = curr = ans = 0
        for i, x in enumerate(nums):
            j = last.get(x, -1)
            small = bisect_right(index, j)  # entries <= j (0 if not on last)
            large = len(index) - small  # entries > j
            s = totalsum - sum(index[:small]) if small <= large else sum(index[small:])
            curr += 2 * (s - j * large) + i - j

            if(j >= 0):
                del index[small - 1]  # idxs[small-1] == j
                totalsum -= j
            index.append(i)
            totalsum += i
            last[x] = i
            ans += curr

        return ans % 1_000_000_007

'''
# Brute force method 


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        Mod = 10**9 + 7
        count = 0 
        
        for i in range(len(nums)):
            s = set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                count += len(s)**2
                
        return count % Mod

        
'''