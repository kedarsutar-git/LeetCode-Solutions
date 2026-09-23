import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1

            else:
                count_map[num] = 1

        arr = []
        for key,value in count_map.items():
            arr.append([value,key])

        arr.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])


        return ans 
             


               
            
        