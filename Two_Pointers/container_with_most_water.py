class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxarr=0
        while l<r:
            arr=(r-l)*min(heights[r],heights[l])
            maxarr=max(maxarr,arr)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxarr