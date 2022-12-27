class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        need = [capacity[i] - rocks[i] for i in range(n)]
        need.sort()
        
        preSum = [0]*n
        preSum[0] = need[0]
        for i in range(1, n):
            preSum[i] = preSum[i-1]+need[i]

        return bisect_right(preSum, additionalRocks)