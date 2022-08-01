#define LB(i) (i&(-i))

typedef struct {
    int *tree;
    int size;
} NumArray;

void numArrayUpdate(NumArray*, int, int);

NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray* obj;
    int i;
    
    obj = calloc(1, sizeof(NumArray));
    if (obj == NULL) {
        return NULL;
    }
    
    obj->tree = calloc(numsSize+1, sizeof(int));
    if (obj->tree == NULL) {
        return NULL;
    }

    obj->size = numsSize;
    
    for (i = 0; i < numsSize; i++) {
        numArrayUpdate(obj, i, nums[i]);
    }

    return obj;
}

void numArrayUpdate(NumArray* obj, int index, int val) {
    val -= (numArraySum(obj, index) - numArraySum(obj, index-1));
    index++;
    
    while (index <= obj->size) {
        obj->tree[index] += val;
        index += LB(index);
    }
}

int numArraySum(NumArray* obj, int index) {
    int result = 0;
    index++;
    while (index > 0) {
        result += obj->tree[index];
        index -= LB(index);
    }

    return result;
}

int numArraySumRange(NumArray* obj, int left, int right) {
    return (numArraySum(obj, right) - numArraySum(obj, left-1));
}

void numArrayFree(NumArray* obj) {
    free(obj->tree);
    free(obj);
}

/**
 * Your NumArray struct will be instantiated and called as such:
 * NumArray* obj = numArrayCreate(nums, numsSize);
 * numArrayUpdate(obj, index, val);
 
 * int param_2 = numArraySumRange(obj, left, right);
 
 * numArrayFree(obj);
*/