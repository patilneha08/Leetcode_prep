class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        h=[]
        res=[]
        for i in points:
            d=math.sqrt((i[0] - 0)**2 + (i[1] - 0)**2)
            heapq.heappush(h,(-d,i))
            if len(h)>k:
                heapq.heappop(h)
        for i in h:
            res.append(i[1])
        return res