class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        _p = Counter(p)
        _s = deque([])

        n = len(p)
        ans = []
        for i in range(len(s)):
            _s.append(s[i])
            if len(_s) > n:
                _s.popleft()
            
            if len(_s) == n:
                if _p == Counter(_s):
                    ans.append(i-n+1)
        return ans