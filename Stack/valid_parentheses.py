class Solution:
    def isValid(self, s: str) -> bool:
        h={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i in h and stack:
                if h[i]!=stack.pop():
                    return False
            else:
                stack.append(i)
        return True if not stack else False