#define max(a,b) (a>b?a:b)
/*
int helper(int* nums, int n, int *result) {
    int current;
    int temp;
        
    current = 1;
    for (int i = 1; i < n; i++) {
        temp = helper(nums, i, result);
        if (nums[i-1] < nums[n-1] && temp + 1 > current) {
            current = temp + 1;
        }
    }
    
    *result = max(*result, current);
    
    return current;
}

int lengthOfLIS(int* nums, int n) {
    int result = 1;
    
    helper(nums, n, &result);
    
    return result;
}
*/

int lengthOfLIS(int* nums, int n) {
    int i, j;
    int LIS[n];
    int result = 1;

    for (i = 0; i < n; i++) {
        LIS[i] = 1;
    }
    
    for (i = 1; i < n; i++) {
        for (j = 0; j < i; j++) {
            if (nums[j] < nums[i] && LIS[j] + 1 > LIS[i]) {
                LIS[i] = LIS[j] + 1;
            }
        }
    }
    
    for (i = 0; i < n; i++) {
        result = max(result, LIS[i]);
    }
    
    return result;
}