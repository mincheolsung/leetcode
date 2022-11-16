class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for i in range(1,n+1):
            for k in range(1,int(n**0.5)+1):
                dp[i] = min(dp[i], dp[i-(k*k)]+1)

        return dp[n]