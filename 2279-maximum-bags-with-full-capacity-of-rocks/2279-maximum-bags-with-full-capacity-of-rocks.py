class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        need = [capacity[i] - rocks[i] for i in range(n)]
        need.sort()

        for i in range(1, n):
            need[i] = need[i-1]+need[i]

        return bisect_right(need, additionalRocks)