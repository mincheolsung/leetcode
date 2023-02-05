class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        _p = Counter(p)
        n = len(p)
        ans = []
        for i in range(len(s)-n+1):
            if (_p == Counter(s[i:i+n])):
                ans.append(i)
                
        return ans