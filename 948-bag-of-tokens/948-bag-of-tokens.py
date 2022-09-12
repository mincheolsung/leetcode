class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        cur = 0
        q = deque(sorted(tokens))
        while q and (q[0] <= power or cur):
            if q[0] <= power:
                cur+=1
                power -= q.popleft()
            else:
                cur-=1
                power += q.pop()
            
            ans = max(ans, cur)
            
        return ans