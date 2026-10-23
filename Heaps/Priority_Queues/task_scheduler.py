class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        h,hp={},[]
        t,q=0,deque()
        for i in tasks:
            h[i]=h.get(i,0)+1
        for j in h.values():
            heapq.heappush(hp,-j)
        while hp or q:
            if q and q[0][1]==t:
                heapq.heappush(hp,q.popleft()[0])
            if hp:
                temp=heapq.heappop(hp)+1
                if temp!=0:
                    q.append((temp,t+n+1))
            t+=1
        return t