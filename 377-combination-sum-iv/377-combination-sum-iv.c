int combinationSum4(int* nums, int numsSize, int target){
    unsigned long long *memo = calloc(target+1, sizeof(unsigned long long));
    if (memo == NULL) {
        return 0;
    }
    memo[0] = 1;
    
    for (int i = 1; i <= target; i++) {
        for (int j = 0; j < numsSize; j++) {
            if (i-nums[j] >= 0) {
                memo[i] = memo[i] + memo[i-nums[j]];
            }
        }
    }

    return memo[target];
}