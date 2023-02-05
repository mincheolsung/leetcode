class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        _p = Counter(p)
        _s = Counter([])
        n = len(p)
        ans = []
        for i in range(len(s)):
            _s[s[i]]+=1
            if i >= n:
                _s[s[i-n]]-=1
                
            if i >= n-1:
                if _p == _s:
                    ans.append(i-n+1)
        return ans