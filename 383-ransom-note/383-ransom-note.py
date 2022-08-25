class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for s in ransomNote:
            if counter[s] < 1:
                return False
            else:
                counter[s]-=1
                
        return True