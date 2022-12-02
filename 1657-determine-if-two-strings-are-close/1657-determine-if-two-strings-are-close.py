class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1 = list(word1)
        word2 = list(word2)
        set1 = set(word1)
        set2 = set(word2)
        
        if set1 != set2:
            return False
        
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        
        if sorted(cnt1.values()) == sorted(cnt2.values()):
            return True
        else:
            return False
        