class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        for i in strs:
            ch=[0]*26
            for j in i:
                ch[ord(j)-ord('a')]+=1
            h[tuple(ch)].append(i)
        return list(h.values())