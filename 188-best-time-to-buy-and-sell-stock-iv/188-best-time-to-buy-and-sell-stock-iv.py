class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[float('-inf')]*(2*k+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
    
        for i in range(1,n+1):
            for j in range(1,2*k+1):
                if j%2:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i-1])
                    
        
        answer = float('-inf')
        for i in range(k+1):
            answer = max(answer, dp[n][2*i])

        return answer