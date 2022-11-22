#define min(a,b) (a<b?a:b)

int numSquares(int n){
    int sqrt_n = sqrt(n);
    int *dp = malloc(4*(n+1));

    for (int i = 0; i < n+1; i++) {
        dp[i] = INT_MAX;
    }

    dp[0] = 0;
    for (int i = 1; i < n+1; i++) {
        for (int k = 1; k < sqrt_n + 1; k++) {
            if (i >= k*k) {
                dp[i] = min(dp[i], dp[i-(k*k)] + 1);
            }
        }
    }

    return dp[n];
}