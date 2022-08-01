

int uniquePaths(int m, int n) {
    int **dp = calloc(m, sizeof(int*));
    if (dp == NULL) {
        return 0;
    }
    
    int i,j;
    
    for (i = 0; i < m; i++) {
        dp[i] = calloc(n, sizeof(int));
        if (dp[i] == NULL) {
            return 0;
        }
    }

    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 1;
                continue;
            }
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    
    return dp[m-1][n-1];
}