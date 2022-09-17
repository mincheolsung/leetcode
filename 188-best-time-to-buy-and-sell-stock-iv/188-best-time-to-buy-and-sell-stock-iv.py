class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[float('-inf')]*(n+1) for _ in range(2*k+1)]

        for i in range(n+1):
            dp[0][i] = 0
    
        for i in range(1,2*k+1):
            for j in range(1,n+1):
                if i%2:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] - prices[j-1])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + prices[j-1])
            
        answer = float('-inf')
        for i in range(k+1):
            answer = max(answer, dp[2*i][n])
    
        return answer