void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int *nums, int start, int end) {
    int i,j;
    
    i = start - 1;
    for (j = start; j < end; j++) {
        if (nums[j] < nums[end]) {
            i++;
            swap(&nums[i], &nums[j]);
        }
    }
    swap(&nums[i+1], &nums[end]);
    return i+1;
}

void quick_sort(int *nums, int start, int end) {
    if (start < end) {
        int pi = partition(nums, start, end);
        
        quick_sort(nums, start, pi-1);
        quick_sort(nums, pi+1, end);
    }
}

void sortColors(int* nums, int numsSize){
    quick_sort(nums, 0, numsSize - 1);
}