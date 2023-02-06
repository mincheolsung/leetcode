class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n, m = len(sentence1), len(sentence2)
        if n != m:
            return False

        for i in range(n):
            found = False
            if sentence1[i] == sentence2[i]:
                continue
            
            for a,b in similarPairs:
                if [sentence1[i], sentence2[i]] == [a,b]:
                    found = True
                    break
                if[sentence1[i], sentence2[i]] == [b,a]:
                    found = True
                    break
            if found:
                continue
            
            return False

        return True