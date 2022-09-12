class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        score = 0
        q = deque(sorted(tokens))
        while q and (q[0] <= power or score):
            if q[0] <= power:
                score+=1
                power -= q.popleft()
            else:
                score-=1
                power += q.pop()
            
            ans = max(ans, score)
            
        return ans