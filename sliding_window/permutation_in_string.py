class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sh1={}
        k=len(s1)
        for i in s1:
            sh1[i]=sh1.get(i,0)+1
        l,sh2=0,{}
        for r in range(len(s2)):
            sh2[s2[r]]=sh2.get(s2[r],0)+1
            if r-l+1<k:
                continue
            else:
                if sh1==sh2:
                    return True
                sh2[s2[l]]-=1
                if sh2[s2[l]]==0:
                    del sh2[s2[l]]
                l+=1
        return False