class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sh,th={},{}
        for i in s:
            sh[i]=1+sh.get(i,0)
        for j in t:
            th[j]=1+th.get(j,0)
        for k in sh:
            if sh[k]!=th.get(k,0):
                return False
        return True