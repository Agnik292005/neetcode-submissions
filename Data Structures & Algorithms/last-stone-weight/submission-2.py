class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            b=-heapq.heappop(heap)
            a=-heapq.heappop(heap)
            if a==b:
                continue
            else:
                b=b-a
                heapq.heappush(heap,-b)
        if heap:
            return -heap[0]
        return 0

        