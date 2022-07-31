#define max(a,b) (a>b?a:b)

int jump(int* nums, int numsSize){
    int i;
    int end = 0;
    int furthest = 0;
    int steps = 0;

    if (numsSize == 1) {
        return 0;
    }

    for (i = 0; i < numsSize-1; i++) {
        furthest = max(furthest, i + nums[i]);
        if (i == end) {
            steps++;
            end = furthest;
        }
    }
    
    return steps;
}