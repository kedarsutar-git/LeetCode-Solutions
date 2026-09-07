class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heap.append(stones[i])

        while len(heap) > 1:
            heap.sort()
            heap.reverse()

            x = heap.pop(0)
            y = heap.pop(0)

            if(x != y):
                heap.append(x - y)

        if(len(heap))== 0:
            return 0
        else:
            return heap[0]