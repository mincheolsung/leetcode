#define max(a,b) (a>b?a:b)
/*
// Recursive
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

// Dynamic programming
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
*/
void replace(int*sub, int len, int target) {
    if (len == 1) {
        if (target <= sub[0]) {
            sub[0] = target;
            return;
        }
    }

    for (int i = 0; i < len-1; i++) {
        if (sub[i] == target) {
            return;
        }

        if (sub[i] < target && target <= sub[i+1]) {
            sub[i+1] = target;
            return;
        }
    }
}

int lengthOfLIS(int* nums, int n) {
    int sub[n];
    int len = 0;
    int i;
    
    len = 1;
    sub[0] = nums[0];
    for (i = 1; i < n; i++) {
        if (sub[len-1] < nums[i]) {
            sub[len] = nums[i];
            len++;
        } else {
            int k = 0;
            while (sub[k] < nums[i]) {
                k++;
            }
            sub[k] = nums[i];
        }
    }

    return len;
}