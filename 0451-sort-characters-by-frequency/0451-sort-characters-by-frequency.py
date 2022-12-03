class Solution:
    def frequencySort(self, s: str) -> str:
        freq = sorted(Counter(s).items(), key = lambda x:(-x[1],x[0]))

        ans = []
        for key,val in freq:
            ans.append(key*val)
            
        return "".join(ans)