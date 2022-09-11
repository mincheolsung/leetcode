class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        q = []
        sum = 0
        result = 0
        for e,s in sorted(zip(efficiency, speed), reverse=1):
            heappush(q,s)
            sum += s
            if len(q) > k:
                sum-=heappop(q)
            result = max(result, sum*e) 
            
        return result % (10**9+7)