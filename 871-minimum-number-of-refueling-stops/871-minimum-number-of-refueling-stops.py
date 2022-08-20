class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        
        num_stations = len(stations)
        dp = [0]*(num_stations+1)
        dp[0] = startFuel

        for i, [position, fuel] in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= position:
                    dp[j+1] = max(dp[j+1], dp[j] + fuel)

        for i in range(len(dp)):
            if dp[i] >= target:
                return i

        return -1
            