import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx=max(piles)
        l,r=1,mx
        while l<=r:
            m=l+(r-l)//2
            temp=0
            for i in range(len(piles)):
                temp+=math.ceil(piles[i]/m)
            if temp>h:
                l=m+1
            elif temp<=h:
                r=m-1
        return l 