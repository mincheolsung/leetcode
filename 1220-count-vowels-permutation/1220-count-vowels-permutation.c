#define a 0
#define e 1
#define i 2
#define o 3
#define u 4
#define MOD(a) ((a)%1000000007ULL)

int countVowelPermutation(int n) {
    int idx;
    unsigned long long *dp[5];

    for (idx = 0; idx < 5; idx++) {
        dp[idx] = calloc(n+1, sizeof(unsigned long long));
        dp[idx][1] = 1;
    }

    for (idx = 2; idx <= n; idx++) {     
        dp[a][idx] = MOD(dp[e][idx-1] + dp[i][idx-1] + dp[u][idx-1]);
        dp[e][idx] = MOD(dp[a][idx-1] + dp[i][idx-1]);   
        dp[i][idx] = MOD(dp[e][idx-1] + dp[o][idx-1]);   
        dp[o][idx] = MOD(dp[i][idx-1]);   
        dp[u][idx] = MOD(dp[i][idx-1] + dp[o][idx-1]);
    }

    return (int)MOD(dp[a][n] + dp[e][n] + dp[i][n] + dp[o][n] + dp[u][n]);;
}