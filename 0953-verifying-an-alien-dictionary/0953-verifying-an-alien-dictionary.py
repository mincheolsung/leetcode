class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = defaultdict(int)
        for i,v in enumerate(order):
            dict[v] = i

        def compare(s1:str, s2:str)->int:
            cnt = 0
            n = min(len(s1), len(s2))
            for i in range(n):
                if dict[s1[i]] < dict[s2[i]]:
                    return 1
                elif dict[s1[i]] > dict[s2[i]]:
                    return -1
                
            if len(s1) <= len(s2):
                return 1
            else:
                return -1
        
        for i in range(len(words)-1):
            if compare(words[i], words[i+1]) < 0:
                return False

        return True