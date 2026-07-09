import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1

            else:
                count_map[num] = 1

        top_keys = heapq.nlargest(k,count_map,key = count_map.get)

        return top_keys

            



             


               
            
        