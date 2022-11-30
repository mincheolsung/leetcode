class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        values = set(counter.values())
        if len(values) != len(counter):
            return False
        return True
        
            