class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        s=0
        maxl,maxr=height[l],height[r]
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                if height[l]<min(maxl,maxr):
                    s+=min(maxl,maxr)-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                if height[r]<min(maxl,maxr):
                    s+=min(maxl,maxr)-height[r]
        return s