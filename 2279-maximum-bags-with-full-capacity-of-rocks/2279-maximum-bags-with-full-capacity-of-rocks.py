class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        need = sorted([capacity[i] - rocks[i] for i in range(n)])
        for i in range(1, n):
            need[i] = need[i-1]+need[i]
        return bisect_right(need, additionalRocks)