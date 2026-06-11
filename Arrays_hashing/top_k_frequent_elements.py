class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h,res={},[]
        for i in nums:
            h[i]=1+h.get(i,0)
        b=[[] for j in range(len(nums)+1)]
        for j in h:
            b[h[j]].append(j)
        for l in range(len(nums),-1,-1):
            for m in b[l]:
                res.append(m)
                if len(res)>=k:
                    return res
