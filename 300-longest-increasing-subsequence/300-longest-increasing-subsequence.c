#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)

int lengthOfLIS(int* nums, int n){
    int i,j;
    int max_lis;
    int *lis;
    
    lis = malloc(n*sizeof(int));
    if (lis == NULL) {
        return 0;
    }
    
    for (i = 0; i < n; i++) {
        lis[i] = 1;
    }
    
    max_lis = lis[0];
    for (i = 1; i < n; i++) {
        for (j = 0; j < i; j++) {
            if (nums[j] < nums[i] && lis[j] + 1 > lis[i]) {
                lis[i] = lis[j] + 1;
            }   
        }
        max_lis = max(max_lis, lis[i]);
    }
    
    return max_lis;
}