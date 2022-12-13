class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[float('inf')]*m for _ in range(n)]
        
        for i in range(n):
            dp[0][i] = matrix[0][i]
            
        for i in range(1,m):
            dp[i][0] = matrix[i][0] + min(dp[i-1][0], dp[i-1][1])
            for j in range(1,n-1):
                dp[i][j] = matrix[i][j] + min([dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]])
            dp[i][n-1] = matrix[i][n-1] + min(dp[i-1][n-2], dp[i-1][n-1])
            
        return min(dp[m-1][:])