class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x=str(x)
        l,r=0,len(x)-1
        while l<=r:
            if x[r]!=x[l]:
                return False
            l+=1
            r-=1
        return True
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=[]
        while x>0:
            n=x%10 
            num.append(n)
            x=x//10
        l,r=0,len(num)-1
        while l<=r:
            if num[l]!=num[r]:
                return False
            l+=1
            r-=1
        return True