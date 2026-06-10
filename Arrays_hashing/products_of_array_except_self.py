class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,pos=1,1
        res=[]
        for i in range(len(nums)):
            res.append(pre)
            pre*=nums[i]
        print(res)
        for j in range(len(nums)-1,-1,-1):
            res[j]=res[j]*pos
            pos*=nums[j]
        return res
