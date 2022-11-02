class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([(start,0)])
        bank = set(bank)
        
        while q:
            current,step = q.popleft()
            if current == end:
                return step
            
            for i in range(len(current)):
                for c in 'ACGT':
                    target = current[:i] + c + current[i+1:]
                    if target in bank:
                        bank.remove(target)
                        q.append((target, step+1))
                        
        return -1