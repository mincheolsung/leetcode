#define _a 0
#define _e 1
#define _i 2
#define _o 3
#define _u 4
#define MOD(a) ((a)%1000000007ULL)

unsigned long long countVowelPermutation(int n) {
    int idx;
    unsigned long long *dp[5];

    for (idx = 0; idx < 5; idx++) {
        dp[idx] = calloc(n+1, sizeof(unsigned long long));
        dp[idx][1] = 1;
    }

    for (idx = 2; idx <= n; idx++) {     
        dp[_a][idx] = MOD(dp[_e][idx-1] + dp[_i][idx-1] + dp[_u][idx-1]);
        dp[_e][idx] = MOD(dp[_a][idx-1] + dp[_i][idx-1]);   
        dp[_i][idx] = MOD(dp[_e][idx-1] + dp[_o][idx-1]);   
        dp[_o][idx] = MOD(dp[_i][idx-1]);   
        dp[_u][idx] = MOD(dp[_i][idx-1] + dp[_o][idx-1]);
    }

    return (int)MOD(dp[_a][n] + dp[_e][n] + dp[_i][n] + dp[_o][n] + dp[_u][n]);;
}