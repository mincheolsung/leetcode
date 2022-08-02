int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int left,right,mid,cnt,i,j;
    
    left = matrix[0][0];
    right = matrix[matrixSize-1][matrixSize-1];

    while (left < right) {
        mid = left + (right-left)/2;
        cnt = 0;
        j = matrixSize - 1;
        for (i = 0; i < matrixSize; i++) {
            while (j >= 0 && matrix[i][j] > mid) {
                j--;
            }
            cnt += j + 1;
        }
        
        if (cnt < k) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return right;
}