from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.h=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.h[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.h[key] or timestamp<self.h[key][0][1]:
            return ""
        l,r=0,len(self.h[key])-1
        while l<=r:
            m=l+(r-l)//2
            if self.h[key][m][1]==timestamp:
                return self.h[key][m][0]
            if self.h[key][m][1]>timestamp:
                r=m-1
            else:
                l=m+1
        return self.h[key][r][0] 