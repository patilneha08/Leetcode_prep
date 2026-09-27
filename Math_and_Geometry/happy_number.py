class Solution:
    def isHappy(self, n: int) -> bool:
        x=set()
        while n!=1:
            num=self.sumsq(n) 
            if num in x:
                return False
            else:
                x.add(num)
            n=num
        return True
    
    def sumsq(self,s):
        t=0
        while s>0:
            temp=s%10
            t=t+(temp**2)
            s=s//10
        return t