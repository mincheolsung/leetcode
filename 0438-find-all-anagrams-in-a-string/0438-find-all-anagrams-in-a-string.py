class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        _p = Counter(p)
        _s = Counter([])
        n = len(p)
        ans = []
        j = 0
        for i in range(len(s)):
            j = i-n+1
            _s[s[i]]+=1

            if j > 0:
                _s[s[j-1]]-=1

            if j >= 0 and _p == _s:
                ans.append(j)

        return ans