class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        values = list(counter.values())
        values.sort()
        
        for i in range(len(values)-1):
            if values[i] == values[i+1]:
                return False
            
        return True
            