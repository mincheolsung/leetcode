class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freqList = [(val,key) for key,val in freq.items()]
        freqList = sorted(freqList, key = lambda x:(-x[0],x[1]))
        
        ans = []
        for freq,key in freqList:
            ans.append(key*freq)
            
        return "".join(ans)