import heapq
from collections import Counter

def topKFrequent(nums, k):
        count = Counter(nums)

        if k >= len(count):
            return list(count.keys())

        heap = []

        for num in count:
            heapq.heappush(heap, (count[num], num))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
        

res = topKFrequent([1,2, 3, 3, 5, 5, 5], 2)
print(res)