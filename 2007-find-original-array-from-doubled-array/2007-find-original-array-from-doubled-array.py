class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        count = Counter(changed)
        changed = deque(sorted(changed))
        length = len(changed)
        while changed:
            n = changed.popleft()
            if count[n] == 0:
                continue
            else:
                count[n]-=1

            if count[2*n] > 0:
                original.append(n)
                count[2*n] -= 1
        
        if len(original)*2 == length: 
            return original
        else:
            return []