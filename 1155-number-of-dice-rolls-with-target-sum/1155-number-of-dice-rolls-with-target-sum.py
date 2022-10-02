class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        dp = [[0]*(target+1) for _ in range(n+1)]
        
        dp[0][0] = 1

        for i in range(1,n+1):
            for j in range(1, target+1):
                for h in range(1, min(j,k)+1):
                    dp[i][j] += dp[i-1][j-h]

        return dp[n][target]%MOD
    
    
    