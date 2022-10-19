class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        sortedCnt = sorted(list(cnt.keys()), key = lambda x : (-cnt[x],x))
        return sortedCnt[:k] 