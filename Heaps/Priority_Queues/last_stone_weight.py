import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>=2:
            t1=heapq.heappop(heap)
            t2=heapq.heappop(heap)
            if t1==t2:
                continue
            if t2>t1:
                heapq.heappush(heap,-(t2-t1))
        return -heap[0] if heap else 0