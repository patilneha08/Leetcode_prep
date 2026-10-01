class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        c=set()
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l+=1
            c.add(s[r])
            longest=max(longest,r-l+1)
        return longest